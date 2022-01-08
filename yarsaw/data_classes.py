from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class BotDetails:
    BotName: str
    BotMaster: str
    BotAge: str
    BotLocation: str
    BotCompany: str
    BotBirthYear: str
    BotBirthDate: str
    BotBirthPlace: str


@dataclass(frozen=True)
class AIResponse:
    AIResponse: str
    BotDetails: BotDetails
    headers: dict


@dataclass(frozen=True)
class Joke:
    error: bool
    category: str
    type: str
    flags: dict
    id: int
    safe: bool
    lang: str
    headers: dict
    setup: str = None
    delivery: str = None
    joke: str = None
