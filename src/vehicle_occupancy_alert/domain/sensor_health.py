from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import StrEnum

from vehicle_occupancy_alert.domain.sensors import SensorReading


class SensorHealth(StrEnum):
    FRESH = "fresh"
    STALE = "stale"
    MISSING = "missing"


@dataclass(frozen=True, slots=True)
class SensorHealthResult:
    health: SensorHealth
    effective_confidence: float
    reason: str


def evaluate_sensor_health(
    reading: SensorReading | None,
    now: datetime,
    max_age: timedelta,
) -> SensorHealthResult:
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    if max_age < timedelta(0):
        raise ValueError("max_age must not be negative")

    if reading is None:
        return SensorHealthResult(
            health=SensorHealth.MISSING,
            effective_confidence=0.0,
            reason="sensor reading is missing",
        )

    if reading.observed_at > now:
        return SensorHealthResult(
            health=SensorHealth.STALE,
            effective_confidence=0.0,
            reason="sensor reading timestamp is in the future",
        )

    if now - reading.observed_at > max_age:
        return SensorHealthResult(
            health=SensorHealth.STALE,
            effective_confidence=0.0,
            reason="sensor reading is stale",
        )

    return SensorHealthResult(
        health=SensorHealth.FRESH,
        effective_confidence=reading.confidence,
        reason="sensor reading is fresh",
    )
