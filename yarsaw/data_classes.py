from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class AIResponse:
    response: str
    server: str
    uid: Union[str, int]


@dataclass(frozen=True)
class Condition:
    mild: int
    critical: int


@dataclass(frozen=True)
class GlobalCovidStats:
    total_cases: int
    total_deaths: int
    total_recovered: int
    total_active: int
    total_closed: int
    condition: Condition


@dataclass(frozen=True)
class Country:
    name: str
    flag: str


@dataclass(frozen=True)
class Closed:
    total: int
    percentage: dict


@dataclass(frozen=True)
class Cases:
    total: int
    recovered: int
    deaths: int
    closed: Closed


@dataclass(frozen=True)
class CountryCovidStats:
    country: Country
    cases: Cases


@dataclass(frozen=True)
class Joke:
    error: bool
    category: str
    type: str
    flags: dict
    id: int
    safe: bool
    lang: str
    setup: str = None
    delivery: str = None
    joke: str = None
