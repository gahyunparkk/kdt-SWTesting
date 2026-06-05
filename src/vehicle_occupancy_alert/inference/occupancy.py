from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum

from vehicle_occupancy_alert.domain.sensors import SensorReading, SensorType


class OccupancyStatus(StrEnum):
    POSSIBLE_PRESENCE = "possible_presence"
    NOT_DETECTED = "not_detected"
    UNKNOWN = "unknown"


@dataclass(frozen=True, slots=True)
class OccupancyInference:
    status: OccupancyStatus
    confidence: float
    supporting_sensors: tuple[SensorType, ...]
    contradicting_sensors: tuple[SensorType, ...]
    evaluated_at: datetime

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")
        if self.evaluated_at.tzinfo is None:
            raise ValueError("evaluated_at must be timezone-aware")


def infer_occupancy(readings: list[SensorReading] | tuple[SensorReading, ...]) -> OccupancyInference:
    if not readings:
        return OccupancyInference(
            status=OccupancyStatus.UNKNOWN,
            confidence=0.0,
            supporting_sensors=(),
            contradicting_sensors=(),
            evaluated_at=datetime.now(UTC),
        )

    supporting: list[SensorReading] = []
    contradicting: list[SensorReading] = []
    for reading in readings:
        if _indicates_presence(reading):
            supporting.append(reading)
        else:
            contradicting.append(reading)

    evaluated_at = max(reading.observed_at for reading in readings)
    if supporting:
        confidence = _presence_confidence(supporting, contradicting)
        status = OccupancyStatus.POSSIBLE_PRESENCE
    else:
        confidence = _combined_confidence(contradicting)
        status = OccupancyStatus.NOT_DETECTED

    return OccupancyInference(
        status=status,
        confidence=round(confidence, 4),
        supporting_sensors=tuple(reading.sensor_type for reading in supporting),
        contradicting_sensors=tuple(reading.sensor_type for reading in contradicting),
        evaluated_at=evaluated_at,
    )


def _indicates_presence(reading: SensorReading) -> bool:
    if reading.sensor_type in {
        SensorType.SEAT_OCCUPANCY,
        SensorType.CABIN_MOTION,
        SensorType.CAMERA_OCCUPANCY,
    }:
        return bool(reading.value)
    if reading.sensor_type is SensorType.SOUND_LEVEL:
        return float(reading.value) >= 55.0
    return False


def _presence_confidence(
    supporting: list[SensorReading],
    contradicting: list[SensorReading],
) -> float:
    support_confidence = _combined_confidence(supporting)
    contradiction_penalty = sum(reading.confidence for reading in contradicting) * 0.15
    return max(0.0, min(1.0, support_confidence - contradiction_penalty))


def _combined_confidence(readings: list[SensorReading]) -> float:
    if not readings:
        return 0.0

    remaining_uncertainty = 1.0
    for reading in readings:
        remaining_uncertainty *= 1.0 - reading.confidence
    return 1.0 - remaining_uncertainty
