from datetime import UTC, datetime

from vehicle_occupancy_alert.domain.sensors import SensorReading, SensorType
from vehicle_occupancy_alert.inference.occupancy import (
    OccupancyStatus,
    infer_occupancy,
)


def _reading(sensor_type: SensorType, value, confidence: float) -> SensorReading:
    return SensorReading(
        sensor_type=sensor_type,
        value=value,
        confidence=confidence,
        observed_at=datetime(2026, 6, 5, 8, 0, tzinfo=UTC),
    )


def test_fr_003_high_confidence_occupancy_signal_creates_possible_presence():
    result = infer_occupancy(
        [
            _reading(SensorType.SEAT_OCCUPANCY, True, 0.95),
            _reading(SensorType.CABIN_MOTION, True, 0.80),
        ]
    )

    assert result.status is OccupancyStatus.POSSIBLE_PRESENCE
    assert result.confidence >= 0.90
    assert SensorType.SEAT_OCCUPANCY in result.supporting_sensors


def test_fr_003_no_occupancy_signals_create_not_detected_result():
    result = infer_occupancy(
        [
            _reading(SensorType.SEAT_OCCUPANCY, False, 0.90),
            _reading(SensorType.CABIN_MOTION, False, 0.85),
        ]
    )

    assert result.status is OccupancyStatus.NOT_DETECTED
    assert result.confidence >= 0.80


def test_nfr_001_contradictory_signals_reduce_inference_confidence():
    result = infer_occupancy(
        [
            _reading(SensorType.SEAT_OCCUPANCY, True, 0.95),
            _reading(SensorType.CABIN_MOTION, False, 0.90),
        ]
    )

    assert result.status is OccupancyStatus.POSSIBLE_PRESENCE
    assert result.confidence < 0.95
    assert result.contradicting_sensors == (SensorType.CABIN_MOTION,)


def test_nfr_001_empty_sensor_set_is_unknown_with_zero_confidence():
    result = infer_occupancy([])

    assert result.status is OccupancyStatus.UNKNOWN
    assert result.confidence == 0.0
