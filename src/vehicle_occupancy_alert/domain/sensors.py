from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Any


class SensorType(StrEnum):
    SEAT_OCCUPANCY = "seat_occupancy"
    CABIN_MOTION = "cabin_motion"
    CABIN_TEMPERATURE = "cabin_temperature"
    SOUND_LEVEL = "sound_level"
    CAMERA_OCCUPANCY = "camera_occupancy"


@dataclass(frozen=True, slots=True)
class SensorReading:
    sensor_type: SensorType
    value: Any
    confidence: float
    observed_at: datetime

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")
        if self.observed_at.tzinfo is None:
            raise ValueError("observed_at must be timezone-aware")
