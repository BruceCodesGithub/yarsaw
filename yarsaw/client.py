from .httpclient import HTTPClient
from .utils import *
import base64
import aiohttp


class Client:
    """Async Client object with functions covering related endpoints.

    Parameters:
    authorization: Your RSA API Key (Positional)
    """
    def __init__(self, authorization):
        self.client = HTTPClient(authorization)
        self.__key__ = authorization

    async def get_covid_stats(self, country=None):
        if country is None:
            params = None
        else:
            params = {"country": country}
        response = await self.client.request("covid", params=params)
        return response

    async def get_ai_response(self, message, *, plan="free", **kwargs):

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
        response = await self.client.request(endpoint, params=params)
        return response

    async def get_weather(self, city):
        return await self.client.request("weather", params={"city": city})

    async def get_image(self, img_type: str):
        type_list = (
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
        if img_type.lower() not in type_list:
            supported_types = ", ".join(type_list)
            raise InvalidArgumentsException(f"Invalid Type. Supported types are: {supported_types}")
        else:
            return await self.client.request("image", params={"type": img_type})

    async def get_fact(self, *, plan, fact_type="all"):
        return await self.client.request(
            f"premium/{plan.lower()}/facts", params={"type": fact_type}
        )

    async def get_joke(self, joke_type="any", blacklist: list = []):
        joke_type_list = (
            "any",
            "dark",
            "pun",
            "spooky",
            "christmas",
            "programming",
            "misc",
        )
        joke_type = joke_type.lower()
        if joke_type not in joke_type_list:
            supported_types = ", ".join(joke_type_list)
            raise InvalidArgumentsException(f"Invalid Type. Supported types are: {supported_types}")
        blist = ""
        if blacklist:

            if "all" in blacklist:
                print("Yay")
                blist = "nsfw&religious&political&racist&sexist&explicit"
            else:
                blist = "&".join(blacklist)
        print(blist)

        return await self.client.request(
            f"joke?blacklist={blist}", params={"type": joke_type}
        )

    async def get_waifu(self, waifu_type, *, plan):
        if not plan.lower() in PLANS:
            raise InvalidPlanException(
                "Invalid Plan. Make sure the plan exists and you specified it in the 'plan' format instead of 'premium/plan'. Eg - 'pro'."
            )
        return await self.client.request(
            f"premium/{plan.lower()}/waifu", params={"type": waifu_type}
        )

    async def canvas(self, method, save_as=None, **kwargs):
        all_methods = [
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
        allowed_combinations = {
            1: [
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
                "changemymind",
            ],
            2: ["bed", "fuse", "kiss", "slap", "spank"],
            3: ["distracted"],
        }
        if method in allowed_combinations[len(kwargs.items())] and all_methods:
            pass
        else:
            raise InvalidArgumentsException(
                "That method either does not exist, or takes more arguments. Try reading the docs and checking if everything is in the right case."
            )
        params = {
            "method": method,
            "txt": kwargs.get("txt", ""),
            "img1": kwargs.get("img1", ""),
            "img2": kwargs.get("img2", ""),
            "img3": kwargs.get("img3", ""),
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.pgamerx.com/v5/canvas",
                headers={"Authorization": self.__key__},
                params=params,
            ) as response:
                try:
                    base = await response.json()
                except aiohttp.client_exceptions.ContentTypeError:
                    return await response.text()
                base = base[0]["base64"]

        if save_as:
            file = open(save_as, 'wb')
            file.write(base64.b64decode((base))) 
            file.close()

            return 200

        return base64.b64decode((base))
