from .errors import *
import string
import random


async def format_joke(joke: dict, format_as="{setup}\n{delivery}") -> str:
    if not "{setup}" in format_as or not "{delivery}" in format_as:
        raise ValueError(
            "'format_as' must contain the '{setup}' and '{devlivery}' values"
        )
    if joke.get("type") == "twopart":
        return format_as.format(setup=joke.get("setup"), delivery=joke.get("delivery"))
    else:
        return joke.get("joke")


async def generate_uid(chars: int = 8, special_chars=False, letters=True):
    characters = string.digits

    if special_chars:
        characters = characters + string.punctuation

    if letters:
        characters = characters + string.ascii_letters

    uid = "".join(random.choice(characters) for i in range(chars))
    return uid


PLANS = {
    "free": "",
    "pro": "premium/pro",
    "ultra": "premium/ultra",
    "biz": "premium/biz",
    "mega": "premium/mega",
}


async def check_res(res):
    if res.status == 200:
        pass
    elif res.status == 401:
        raise InvalidAPIKeyException(await res.text())
    elif res.status == 403:
        raise InvalidAPIKeyException(await res.text())
    elif res.status == 429:
        raise RateLimited(await res.text())


CANVAS_METHODS = [
    "affect",
    "beautiful",
    "wanted",
    "delete",
    "trigger",
    "facepalm",
    "blur",
    "hitler",
    "kiss",
    "jail",
    "invert",
    "jokeOverHead",
    "bed",
    "fuse",
    "kiss",
    "slap",
    "spank",
    "distracted",
    "changemymind",
]


JOKE_TYPES = (
    "any",
    "dark",
    "pun",
    "spooky",
    "christmas",
    "programming",
    "misc",
)

IMAGE_TYPES = (
    "aww",
    "duck",
    "dog",
    "cat",
    "memes",
    "dankmemes",
    "holup",
    "art",
    "harrypottermemes",
    "facepalm",
)

WAIFU_TYPES = ("waifu", "neko", "shinobu", "megumin", "bully", "cuddle")

FACT_TYPES = ("all", "dog", "cat", "space", "covid", "computer", "food", "emoji")