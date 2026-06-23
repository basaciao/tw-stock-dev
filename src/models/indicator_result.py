from dataclasses import dataclass


@dataclass
class IndicatorResult:

    rsi: float

    macd: float

    signal: float

    histogram: float

    k: float

    d: float
