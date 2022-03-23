from .exceptions import *
import string
import random
from typing import Union
from .data_classes import *


# format_joke and generate_uid were inspired by nerdguyahmad's randomstuff.py


def format_joke(joke: Joke, format_as="{setup}\n{delivery}") -> str:
    """
    Support function for :func:`Client.get_joke`. Auto-format a joke. If its a single type of joke, it returns the joke itself. If its a two-part joke, it returns the setup and delivery, separated by a newline or a character you choose.

    Parameters
    ----------

    joke: :class:`Joke`
        The joke to format.

    format_as: Optional[:class:`str`]
        The format to use. Defaults to ``"{setup}\\n{delivery}"``.

    Returns
    -------

    :class:`str`
        The formatted joke.
    """
    if not isinstance(joke, Joke):
        raise TypeError(f"Expected joke to be of type Joke, got {type(joke)}")
    if "{setup}" in format_as and "{delivery}" in format_as:
        if joke.type == "twopart":
            return format_as.format(setup=joke.setup, delivery=joke.delivery)
        return joke.joke
    raise ValueError("The format_as string must contain {setup} and {delivery}")


def generate_uid(chars: int = 8, letters=True, special_chars=False):
    """
    Support function for :func:`Client.get_ai_response`. Generates a random string of characters to be used as a unique identifier for a user.

    Parameters
    ----------

    chars: Optional[:class:`int`]
        The number of characters to generate. Defaults to 8.

    letters: Optional[:class:`bool`]
        Whether or not to include letters. Defaults to True.

    special_chars: Optional[:class:`bool`]
        Whether or not to include special characters. Defaults to False.

    Returns
    -------

    :class:`str`
        The generated UID.
    """
    characters = string.digits

    if special_chars:
        characters = characters + string.punctuation

    if letters:
        characters = characters + string.ascii_letters

    uid = "".join(random.choice(characters) for i in range(chars))
    return uid


# check_res was inspired by randomstuff.py from nerdguyahmad


async def check_res(res):
    if res.status == 200:
        pass
    elif res.status == 401:
        raise InvalidAPIKey(await res.text())
    elif res.status == 403:
        try:
            json_response = await res.json()
        except:
            raise InvalidAPIKey(await res.text())
        else:
            raise InvalidAPIKey(json_response["message"])
    elif res.status == 429:
        raise RateLimited(await res.text())
    elif res.status == 502:
        json_response = await res.json()
        try:
            response = json_response["messages"]
            info = json_response["info"]
        except:
            raise BadGateway(await res.text())
        else:
            raise BadGateway(response, info)
    else:
        raise RuntimeError(await res.text())


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

FACT_TYPES = ("all", "dog", "cat", "space", "covid", "computer", "food", "emoji")

ANIME_TYPES = (
    "happy",
    "hi",
    "kiss",
    "hug",
    "punch",
    "pat",
    "slap",
    "nervous",
    "run",
    "cry",
)

ANIMAL_TYPES = (
    "DOG",
    "CAT",
    "WOLF",
    "FOX",
)

SEARCH_TYPES = ("hot", "top", "new", "rising")
