from datetime import UTC, datetime

from vehicle_occupancy_alert.domain.vehicle_state import (
    VehicleSignalSnapshot,
    VehicleState,
    derive_vehicle_state,
)


def test_fr_001_vehicle_is_moving_when_motion_is_reported():
    snapshot = VehicleSignalSnapshot(
        ignition_on=True,
        speed_kph=12.5,
        driver_door_open=False,
        observed_at=datetime(2026, 6, 5, 8, 0, tzinfo=UTC),
    )

    assert derive_vehicle_state(snapshot) is VehicleState.MOVING


def test_fr_001_vehicle_is_recently_stopped_when_ignition_is_on_and_driver_door_opens():
    snapshot = VehicleSignalSnapshot(
        ignition_on=True,
        speed_kph=0.0,
        driver_door_open=True,
        observed_at=datetime(2026, 6, 5, 8, 0, tzinfo=UTC),
    )

    assert derive_vehicle_state(snapshot) is VehicleState.RECENTLY_STOPPED


def test_fr_001_vehicle_is_parked_when_stationary_with_ignition_off():
    snapshot = VehicleSignalSnapshot(
        ignition_on=False,
        speed_kph=0.0,
        driver_door_open=False,
        observed_at=datetime(2026, 6, 5, 8, 0, tzinfo=UTC),
    )

    assert derive_vehicle_state(snapshot) is VehicleState.PARKED
