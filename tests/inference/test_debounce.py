from datetime import UTC, datetime, timedelta

from vehicle_occupancy_alert.inference.debounce import DebounceWindow
from vehicle_occupancy_alert.inference.occupancy import (
    OccupancyInference,
    OccupancyStatus,
)


def _inference(status: OccupancyStatus, confidence: float, seconds: int) -> OccupancyInference:
    return OccupancyInference(
        status=status,
        confidence=confidence,
        supporting_sensors=(),
        contradicting_sensors=(),
        evaluated_at=datetime(2026, 6, 5, 8, 0, tzinfo=UTC) + timedelta(seconds=seconds),
    )


def test_fr_008_short_transient_presence_does_not_stabilize():
    debounce = DebounceWindow(
        required_status=OccupancyStatus.POSSIBLE_PRESENCE,
        minimum_duration=timedelta(seconds=10),
        minimum_confidence=0.70,
    )

    result = debounce.update(_inference(OccupancyStatus.POSSIBLE_PRESENCE, 0.85, 0))
    result = debounce.update(_inference(OccupancyStatus.NOT_DETECTED, 0.90, 3))

    assert result.is_stable is False
    assert result.stable_since is None


def test_fr_008_presence_stabilizes_after_configured_duration():
    debounce = DebounceWindow(
        required_status=OccupancyStatus.POSSIBLE_PRESENCE,
        minimum_duration=timedelta(seconds=10),
        minimum_confidence=0.70,
    )

    debounce.update(_inference(OccupancyStatus.POSSIBLE_PRESENCE, 0.80, 0))
    result = debounce.update(_inference(OccupancyStatus.POSSIBLE_PRESENCE, 0.82, 11))

    assert result.is_stable is True
    assert result.stable_since == datetime(2026, 6, 5, 8, 0, tzinfo=UTC)


def test_fr_008_low_confidence_presence_resets_debounce_window():
    debounce = DebounceWindow(
        required_status=OccupancyStatus.POSSIBLE_PRESENCE,
        minimum_duration=timedelta(seconds=10),
        minimum_confidence=0.70,
    )

    debounce.update(_inference(OccupancyStatus.POSSIBLE_PRESENCE, 0.80, 0))
    result = debounce.update(_inference(OccupancyStatus.POSSIBLE_PRESENCE, 0.40, 11))

    assert result.is_stable is False
    assert result.stable_since is None
