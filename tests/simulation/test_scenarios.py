from datetime import UTC, datetime

from vehicle_occupancy_alert.domain.sensors import SensorType
from vehicle_occupancy_alert.domain.vehicle_state import VehicleState
from vehicle_occupancy_alert.simulation.scenarios import ScenarioBuilder


def test_fr_012_simulation_scenario_is_deterministic():
    start = datetime(2026, 6, 5, 8, 0, tzinfo=UTC)

    first = (
        ScenarioBuilder(start)
        .vehicle(ignition_on=False, speed_kph=0.0, driver_door_open=False)
        .sensor(SensorType.SEAT_OCCUPANCY, True, confidence=0.95, offset_seconds=2)
        .build()
    )
    second = (
        ScenarioBuilder(start)
        .vehicle(ignition_on=False, speed_kph=0.0, driver_door_open=False)
        .sensor(SensorType.SEAT_OCCUPANCY, True, confidence=0.95, offset_seconds=2)
        .build()
    )

    assert first == second
    assert first.vehicle_state is VehicleState.PARKED
    assert first.sensor_readings[0].observed_at == datetime(2026, 6, 5, 8, 0, 2, tzinfo=UTC)
