from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class VehicleState(StrEnum):
    MOVING = "moving"
    RECENTLY_STOPPED = "recently_stopped"
    PARKED = "parked"
    POWERED_OFF = "powered_off"


@dataclass(frozen=True, slots=True)
class VehicleSignalSnapshot:
    ignition_on: bool
    speed_kph: float
    driver_door_open: bool
    observed_at: datetime

    def __post_init__(self) -> None:
        if self.speed_kph < 0:
            raise ValueError("speed_kph must not be negative")
        if self.observed_at.tzinfo is None:
            raise ValueError("observed_at must be timezone-aware")


def derive_vehicle_state(snapshot: VehicleSignalSnapshot) -> VehicleState:
    if snapshot.speed_kph > 0:
        return VehicleState.MOVING
    if snapshot.ignition_on and snapshot.driver_door_open:
        return VehicleState.RECENTLY_STOPPED
    if snapshot.ignition_on:
        return VehicleState.RECENTLY_STOPPED
    if snapshot.driver_door_open:
        return VehicleState.POWERED_OFF
    return VehicleState.PARKED
