from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Any

from vehicle_occupancy_alert.domain.sensors import SensorReading, SensorType
from vehicle_occupancy_alert.domain.vehicle_state import (
    VehicleSignalSnapshot,
    VehicleState,
    derive_vehicle_state,
)


@dataclass(frozen=True, slots=True)
class Scenario:
    start: datetime
    vehicle_snapshot: VehicleSignalSnapshot
    vehicle_state: VehicleState
    sensor_readings: tuple[SensorReading, ...]


@dataclass(slots=True)
class ScenarioBuilder:
    start: datetime
    _vehicle_snapshot: VehicleSignalSnapshot | None = None
    _sensor_readings: list[SensorReading] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.start.tzinfo is None:
            raise ValueError("start must be timezone-aware")

    def vehicle(
        self,
        *,
        ignition_on: bool,
        speed_kph: float,
        driver_door_open: bool,
        offset_seconds: int = 0,
    ) -> ScenarioBuilder:
        self._vehicle_snapshot = VehicleSignalSnapshot(
            ignition_on=ignition_on,
            speed_kph=speed_kph,
            driver_door_open=driver_door_open,
            observed_at=self.start + timedelta(seconds=offset_seconds),
        )
        return self

    def sensor(
        self,
        sensor_type: SensorType,
        value: Any,
        *,
        confidence: float,
        offset_seconds: int = 0,
    ) -> ScenarioBuilder:
        self._sensor_readings.append(
            SensorReading(
                sensor_type=sensor_type,
                value=value,
                confidence=confidence,
                observed_at=self.start + timedelta(seconds=offset_seconds),
            )
        )
        return self

    def build(self) -> Scenario:
        vehicle_snapshot = self._vehicle_snapshot or VehicleSignalSnapshot(
            ignition_on=False,
            speed_kph=0.0,
            driver_door_open=False,
            observed_at=self.start,
        )
        return Scenario(
            start=self.start,
            vehicle_snapshot=vehicle_snapshot,
            vehicle_state=derive_vehicle_state(vehicle_snapshot),
            sensor_readings=tuple(self._sensor_readings),
        )
