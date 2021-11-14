from .httpclient import HTTPClient
from .utils import *
import base64
import aiohttp


class Client:
    """
    Represents an async client object used to connect with the API.

    Parameters
    -------------
    authorization: :class:`str`
        Your Random Stuff API Key to be used to authorize the connection.
    """

    def __init__(self, authorization):
        self._client = HTTPClient(authorization.strip())
        self.__key = authorization

    async def get_ai_response(self, message, *, plan="free", **kwargs) -> list:
        """
        Fetches ai responses from the API.

        Parameters
        -------------
        message: :class:`str`
            The message to be sent to the API.
        plan: Optional[:class:`str`]
            The plan you bought the API with, if you did.

        Returns
        -------------
        :class:`list`
            A list of responses from the API.
        
        """

        params = {
            "message": message,
            "server": kwargs.get("server", "main"),
            "uid": kwargs.get("uid", 69),
            "bot_name": kwargs.get("name", "Random Stuff API"),
            "bot_master": kwargs.get("master", "PGamerX"),
            "bot_gender": kwargs.get("gender", "Male"),
            "bot_age": kwargs.get("age", "19"),
            "bot_company": kwargs.get("company", "PGamerX Studio"),
            "bot_location": kwargs.get("location", "India"),
            "bot_email": kwargs.get("email", "admin@pgamerx.com"),
            "bot_build": kwargs.get("build", "Public"),
            "bot_birth_year": kwargs.get("birth_year", "2002"),
            "bot_birth_date": kwargs.get("birth_date", "1st January 2002"),
            "bot_birth_place": kwargs.get("birth_place", "India"),
            "bot_favorite_color": kwargs.get("favorite_color", "Blue"),
            "bot_favorite_book": kwargs.get("favorite_book", "Harry Potter"),
            "bot_favorite_band": kwargs.get("favorite_band", "Imagine Doggos"),
            "bot_favorite_artist": kwargs.get("favorite_artist", "Eminem"),
            "bot_favorite_actress": kwargs.get("favorite_actress", "Emma Watson"),
            "bot_favorite_actor": kwargs.get("favorite_actor", "Jim Carrey"),
        }
        endpoint = f"premium/{plan.lower()}/ai" if plan.lower() != "free" else "ai"
        if plan.lower() not in PLANS:
            raise InvalidPlanException(
                "Invalid Plan. Make sure the plan exists and you specified it in the 'plan' format instead of 'premium/plan'. Eg - 'pro'."
            )
        response = await self._client.request(endpoint, params=params)
        return response

    async def canvas(
        self, method, save_to=None, txt=None, text=None, img1=None, img2=None, img3=None
    ) -> bytes:
        """
        Edit Images with the API.

        Parameters
        -------------
        method: :class:`str`
            The method to be used to edit the image.

            **Allowed Methods**:

                - Method(s) in which only 1 image is required: "affect", "beautiful", "wanted", "delete", "trigger", "facepalm", "blur", "hitler", "kiss", "jail", "invert", "jokeOverHead"
                - Method(s) in which 2 images are required: "bed", "fuse" , "kiss", "slap", "spank"
                - Method(s) in which 3 images are required: "distracted"
                - Method(s) in which only Text is required: "changemymind"

        save_to: Optional[:class:`str`]
            The path to save the edited image to. If not specified, the edited image will be returned as bytes.

        txt: Optional[:class:`str`]
            The text required for your method.

        text: Optional[:class:`str`]
            The text required for your method. Alias of txt.

        img1: Optional[:class:`str`]
            The path/link to the first image.

        img2: Optional[:class:`str`]
            The path/link to the second image.

        img3: Optional[:class:`str`]
            The path/link to the third image.

        Returns
        -------------
        Union[:class:`bytes`, :class:`io.BufferedImage`]
            If save_to is not specified, the edited image will be returned as bytes.
            If save_to is specified, the edited image will be saved to the specified path, and will return the image.

        """

        if method.lower() not in CANVAS_METHODS:
            supported_methods = ", ".join(CANVAS_METHODS)
            raise ValueError(
                f"That method does not exist! Supported Methods: {supported_methods}"
            )

        params = {
            "method": method,
            "txt": txt or text or "",
            "img1": img1 or "",
            "img2": img2 or "",
            "img3": img3 or "",
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.pgamerx.com/v5/canvas",
                headers={"Authorization": self.__key},
                params=params,
            ) as response:
                try:
                    base = await response.json()
                except aiohttp.client_exceptions.ContentTypeError:
                    return await response.text()
                base = base[0]["base64"]

        if save_to:
            file = open(save_to, "wb")
            file.write(base64.b64decode((base)))
            file.close()

            return file

        return base64.b64decode((base))

    async def get_covid_stats(self, country=None) -> dict:
        """
        Fetch covid stats from the API.

        Parameters
        -------------
        country: Optional[:class:`str`]
            The country to fetch stats for.
            
        Returns
        -------------
        :class:`dict`
            A dictionary containing the stats.
        """
        if country is None:
            params = None
        else:
            params = {"country": country}
        return await self._client.request("covid", params=params)

    async def get_covid_stats_by_country(self, country) -> dict:
        """
        Fetch covid stats from the API by country.

        Parameters
        -------------
        country: :class:`str`
            The country to fetch stats for.

        Returns
        -------------
        :class:`dict`
            A dictionary containing the stats.
        """
        return await self._client.request("covid", params={"country": country})

    async def get_fact(self, *, plan, fact_type="all"):
        """
        Fetches facts from the API.

        Parameters
        -------------
        plan: :class:`str`
            The plan you bought to use the API.

        fact_type: Optional[:class:`str`]
            The type of fact you want to fetch.
            Allowed Values: "all", "dog", "cat", "space", "covid", "computer", "food", "emoji"
        """
        if plan.lower() not in PLANS:
            raise InvalidPlanException(
                "Invalid Plan. Make sure the plan exists and you specified it in the 'plan' format instead of 'premium/plan'. Eg - 'pro'."
            )
        if fact_type.lower() not in FACT_TYPES:
            raise ValueError(
                "Invalid fact type! Allowed types: all, dog, cat, space, covid, computer, food, emoji"
            )
        return await self._client.request(
            f"premium/{plan.lower()}/facts", params={"type": fact_type}
        )

    async def get_image(self, img_type: str) -> list:
        """
        Fetches images from the API.

        Parameters
        -------------
        img_type: :class:`str`
            The type of image you want to fetch.
            Allowed Values: "aww", "duck", "dog", "cat", "memes", "dankmemes", "holup", "art", "harrypottermemes", "facepalm"

        Returns
        -------------
        :class:`list`
            A list containing the image(s).
        """
        if img_type.lower() not in IMAGE_TYPES:
            supported_types = ", ".join(IMAGE_TYPES)
            raise ValueError(f"Invalid Type. Supported types are: {supported_types}")
        else:
            return await self._client.request("image", params={"type": img_type})

    async def get_joke(self, joke_type="any", blacklist: list = []) -> dict:
        """
        Fetches jokes from the API.

        Parameters
        -------------
        joke_type: Optional[:class:`str`]
            The type of joke you want to fetch.
            Allowed Values: "any", "dark", "pun", "spooky", "christmas", "programming", "misc"

        blacklist: Optional[:class:`list`]
            A list of types jokes you want to blacklist.
            Allowed Values: "all", "nsfw", "religious", "political", "racist", "sexist", "explicit"

        Returns
        -------------
        :class:`dict`
            A dictionary containing the joke.
        """
        joke_type = joke_type.lower()
        if joke_type not in JOKE_TYPES:
            supported_types = ", ".join(JOKE_TYPES)
            raise ValueError(f"Invalid Type. Supported types are: {supported_types}")
        blist = ""
        if blacklist:

            if "all" in blacklist:
                print("Yay")
                blist = "nsfw&religious&political&racist&sexist&explicit"
            else:
                blist = "&".join(blacklist)
        print(blist)

        return await self._client.request(
            f"joke?blacklist={blist}", params={"type": joke_type}
        )

    async def get_safe_joke(self, joke_type="any") -> dict:
        """
        Fetches safe jokes from the API. These jokes are family-friendly.

        Parameters
        -------------
        joke_type: Optional[:class:`str`]
            The type of joke you want to fetch.
            Allowed Values: "any", "dark", "pun", "spooky", "christmas", "programming", "misc"

        Returns
        -------------
        :class:`dict`
            A dictionary containing the joke.
        """

        joke = await self.get_joke()
        while joke["safe"] != True:
            joke = await self.get_joke()
        return joke

    async def get_waifu(self, waifu_type, *, plan):
        """
        Fetches waifus from the API.

        Parameters
        -------------
        waifu_type: :class:`str`
            The type of waifu you want to fetch.
            Allowed Values: "waifu", "neko", "shinobu", "megumin", "bully", "cuddle"

        plan: :class:`str`
            The plan you bought to use the API.
        """
        if not plan.lower() in PLANS:
            raise InvalidPlanException(
                "Invalid Plan. Make sure the plan exists and you specified it in the 'plan' format instead of 'premium/plan'. Eg - 'pro'."
            )
        if not waifu_type.lower() in WAIFU_TYPES:
            supported_types = ", ".join(WAIFU_TYPES)
            raise ValueError(
                f"Invalid Waifu Type. Supported types are: {supported_types}"
            )
        return await self._client.request(
            f"premium/{plan.lower()}/waifu", params={"type": waifu_type.lower()}
        )

    async def get_weather(self, city) -> list:
        """
        Fetches weather data from the API.

        Parameters
        -------------
        city: :class:`str`
            The city you want to fetch weather for.

        Returns
        -------------
        :class:`list`
            A list containing the weather data.
        """
        return await self._client.request("weather", params={"city": city})

    async def disconnect(self):
        """
        Disconnects the client from the API.
        """
        await self._client.close()

    async def restart(self):
        """
        Restarts the client's connection with the API.
        """
        self._client = HTTPClient(self.__key)

    async def connect(self):
        """
        Connects the client to the API, incase it's not already connected.
        """
        if self._client:
            pass
        else:
            self._client = HTTPClient(self.__key)