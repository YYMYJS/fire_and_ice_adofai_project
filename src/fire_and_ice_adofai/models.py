from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Beat:
    index: int
    time: float
    strength: float = 1.0


@dataclass(slots=True)
class AudioAnalysis:
    bpm: float
    offset: float
    beats: list[Beat] = field(default_factory=list)


@dataclass(slots=True)
class ChartPlan:
    bpm: float
    offset: float
    angle_data: list[int]
