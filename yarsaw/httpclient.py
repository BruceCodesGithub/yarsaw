import aiohttp
from .utils import check_res
from dataclasses import dataclass


@dataclass(frozen=True)
class Response:
    body: dict
    headers: dict


class HTTPClient:
    def __init__(self, authorization: str, key):
        if not isinstance(authorization, str):
            raise TypeError(
                "Expected authorization to be str, got {}".format(type(authorization))
            )
        self.__auth = authorization
        if not isinstance(key, str):
            raise TypeError("Expected key to be str, got {}".format(type(key)))
        self.__key = key
        self._base = "https://random-stuff-api.p.rapidapi.com"
        self._session = aiohttp.ClientSession()

    async def request(self, endpoint, *, params=None):
        if params is None:
            params = {}

        try:
            response = await self._session.get(
                f"{self._base}/{endpoint}",
                headers={
                    "Authorization": self.__auth,
                    "X-RapidAPI-Key": self.__key,
                    "X-RapidAPI-Host": "random-stuff-api.p.rapidapi.com",
                },
                params=params,
            )
        except aiohttp.client_exceptions.ClientConnectorError:
            raise ConnectionError("Could not connect to API.")
        else:
            await check_res(response)
            try:
                return Response(await response.json(), response.headers)
            except aiohttp.client_exceptions.ContentTypeError:
                raise RuntimeError(await response.text())

    async def disconnect(self):
        await self._session.close()
