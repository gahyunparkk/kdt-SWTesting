from datetime import UTC, datetime, timedelta

from vehicle_occupancy_alert.domain.sensor_health import SensorHealth, evaluate_sensor_health
from vehicle_occupancy_alert.domain.sensors import SensorReading, SensorType


def test_fr_009_missing_sensor_reading_is_marked_missing_with_zero_confidence():
    result = evaluate_sensor_health(
        reading=None,
        now=datetime(2026, 6, 5, 8, 1, tzinfo=UTC),
        max_age=timedelta(seconds=30),
    )

    assert result.health is SensorHealth.MISSING
    assert result.effective_confidence == 0.0


def test_fr_009_stale_sensor_reading_is_marked_stale_and_reduces_confidence():
    reading = SensorReading(
        sensor_type=SensorType.CABIN_TEMPERATURE,
        value=33.5,
        confidence=0.9,
        observed_at=datetime(2026, 6, 5, 8, 0, tzinfo=UTC),
    )

    result = evaluate_sensor_health(
        reading=reading,
        now=datetime(2026, 6, 5, 8, 1, tzinfo=UTC),
        max_age=timedelta(seconds=30),
    )

    assert result.health is SensorHealth.STALE
    assert result.effective_confidence == 0.0


def test_nfr_001_fresh_sensor_reading_keeps_reported_confidence():
    reading = SensorReading(
        sensor_type=SensorType.CABIN_TEMPERATURE,
        value=33.5,
        confidence=0.9,
        observed_at=datetime(2026, 6, 5, 8, 0, 45, tzinfo=UTC),
    )

    result = evaluate_sensor_health(
        reading=reading,
        now=datetime(2026, 6, 5, 8, 1, tzinfo=UTC),
        max_age=timedelta(seconds=30),
    )

    assert result.health is SensorHealth.FRESH
    assert result.effective_confidence == 0.9
