from .exceptions import *
import string
import random
from typing import Union
from .data_classes import *


class Utils:
    def format_joke(
        self, joke: Union[dict, Joke], format_as="{setup}\n{delivery}"
    ) -> str:
        """
        Support function for get_joke. Auto-format a joke. If its a single type of joke, it returns the joke itself. If its a two-part joke, it returns the setup and delivery, separated by a newline or a character you choose.

        Parameters
        ----------

        joke: Union[:class:`dict`, :class:`Joke`]
            The joke to format.

        format_as: Optional[:class:`str`]
            The format to use. Defaults to ``"{setup}\\n{delivery}"``.

        Returns
        -------

        :class:`str`
            The formatted joke.
        """
        if not "{setup}" in format_as:
            raise ValueError(
                "'format_as' must contain the '{setup}' and '{devlivery}' or '{punchline}' values"
            )
        elif not "{delivery}" in format_as:
            if not "{punchline}" in format_as:
                raise ValueError(
                    "'format_as' must contain the '{setup}' and '{devlivery}' or '{punchline}' values"
                )
            else:
                if isinstance(joke, dict):
                    if joke.get("type") == "twopart":
                        return format_as.format(
                            setup=joke.get("setup"), punchline=joke.get("delivery")
                        )
                    else:
                        return joke.get("joke")
                elif isinstance(joke, Joke):
                    if joke.type == "twopart":
                        return format_as.format(
                            setup=joke.setup, punchline=joke.delivery
                        )
                    else:
                        return joke.joke
                else:
                    raise TypeError("'joke' must be a dict or Joke object")

        if isinstance(joke, dict):
            if joke.get("type") == "twopart":
                return format_as.format(
                    setup=joke.get("setup"), delivery=joke.get("delivery")
                )
            else:
                return joke.get("joke")
        elif isinstance(joke, Joke):
            if joke.type == "twopart":
                return format_as.format(setup=joke.setup, delivery=joke.delivery)
            else:
                return joke.joke
        else:
            raise TypeError("'joke' must be a dict or Joke object")

    def generate_uid(self, chars: int = 8, letters=True, special_chars=False):
        """
        Support function for get_ai_response. Generates a random string of characters to be used as a unique identifier for a user.

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


async def check_res(res):
    if res.status == 200:
        pass
    elif res.status == 401:
        raise InvalidAPIKeyException(await res.text())
    elif res.status == 403:
        try:
            json_response = await res.json()
        except:
            raise InvalidAPIKeyException(await res.text())
        else:
            raise InvalidAPIKeyException(json_response["message"])
    elif res.status == 429:
        raise RateLimited(await res.text())
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
