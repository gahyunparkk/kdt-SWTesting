from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta

from vehicle_occupancy_alert.inference.occupancy import (
    OccupancyInference,
    OccupancyStatus,
)


@dataclass(frozen=True, slots=True)
class DebounceResult:
    is_stable: bool
    stable_since: datetime | None
    latest: OccupancyInference


@dataclass(slots=True)
class DebounceWindow:
    required_status: OccupancyStatus
    minimum_duration: timedelta
    minimum_confidence: float
    _candidate_since: datetime | None = None

    def __post_init__(self) -> None:
        if self.minimum_duration < timedelta(0):
            raise ValueError("minimum_duration must not be negative")
        if not 0.0 <= self.minimum_confidence <= 1.0:
            raise ValueError("minimum_confidence must be between 0.0 and 1.0")

    def update(self, inference: OccupancyInference) -> DebounceResult:
        if self._matches(inference):
            if self._candidate_since is None:
                self._candidate_since = inference.evaluated_at
            is_stable = inference.evaluated_at - self._candidate_since >= self.minimum_duration
            return DebounceResult(
                is_stable=is_stable,
                stable_since=self._candidate_since if is_stable else None,
                latest=inference,
            )

        self._candidate_since = None
        return DebounceResult(
            is_stable=False,
            stable_since=None,
            latest=inference,
        )

    def _matches(self, inference: OccupancyInference) -> bool:
        return (
            inference.status is self.required_status
            and inference.confidence >= self.minimum_confidence
        )
