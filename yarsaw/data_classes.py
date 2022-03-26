from dataclasses import dataclass


@dataclass(frozen=True)
class APIInfo:
    requests_limit: int
    requests_remaining: int
    reset_time: int


@dataclass(frozen=True)
class BotDetails:
    bot_name: str
    bot_master: str
    bot_age: str
    bot_location: str
    bot_company: str
    bot_birth_year: str
    bot_birth_date: str
    bot_birth_place: str


@dataclass(frozen=True)
class AIResponse:
    response: str
    bot_details: BotDetails
    api_info: APIInfo


@dataclass(frozen=True)
class Joke:
    joke: str
    tags: list
    api_info: APIInfo

@dataclass(frozen=True)
class RedditPost:
    id: str
    type: str
    title: str
    author: str
    url: str
    image: str
    gallery: bool
    text: str
    thumbnail: str
    subreddit: str
    nsfw: bool
    spoiler: bool
    created_at: int
    upvotes: int
    downvotes: int
    upvote_ratio: float
    api_info: APIInfo


@dataclass(frozen=True)
class AnimalImage:
    images: list
    api_info: APIInfo

@dataclass(frozen=True)
class AnimeGIF:
    title: str
    thumbnail: str
    image: str
    api_info: APIInfo

@dataclass(frozen=True)
class CanvasResponse:
    base64: str
    decoded_base64: str
    api_info: APIInfo


@dataclass(frozen=True)
class Waifu:
    url: str
    api_info: APIInfo


@dataclass(frozen=True)
class Fact:
    fact: str
    api_info: APIInfo
