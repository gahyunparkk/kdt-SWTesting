from datetime import UTC, datetime

import pytest

from vehicle_occupancy_alert.domain.sensors import SensorReading, SensorType


def test_fr_002_sensor_reading_keeps_type_value_confidence_and_timestamp():
    observed_at = datetime(2026, 6, 5, 8, 0, tzinfo=UTC)

    reading = SensorReading(
        sensor_type=SensorType.SEAT_OCCUPANCY,
        value=True,
        confidence=0.92,
        observed_at=observed_at,
    )

    assert reading.sensor_type is SensorType.SEAT_OCCUPANCY
    assert reading.value is True
    assert reading.confidence == 0.92
    assert reading.observed_at == observed_at


def test_fr_009_sensor_reading_rejects_confidence_below_zero():
    with pytest.raises(ValueError, match="confidence"):
        SensorReading(
            sensor_type=SensorType.CABIN_MOTION,
            value=True,
            confidence=-0.01,
            observed_at=datetime(2026, 6, 5, 8, 0, tzinfo=UTC),
        )


def test_fr_009_sensor_reading_rejects_confidence_above_one():
    with pytest.raises(ValueError, match="confidence"):
        SensorReading(
            sensor_type=SensorType.CABIN_MOTION,
            value=True,
            confidence=1.01,
            observed_at=datetime(2026, 6, 5, 8, 0, tzinfo=UTC),
        )
