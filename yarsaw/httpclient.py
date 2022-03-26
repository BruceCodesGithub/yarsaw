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
            raise TypeError(f"Expected authorization to be str, got {type(authorization)}")
        self.__auth = authorization
        if not isinstance(key, str):
            raise TypeError(f"Expected key to be str, got {type(key)}")
        self.__key = key
        self._base = "https://random-stuff-api.p.rapidapi.com"
        self._session = aiohttp.ClientSession()

    async def request(self, endpoint, *, params=None) -> Response:
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
        except aiohttp.client_exceptions.ClientConnectorError as e:
            raise ConnectionError("Could not connect to API.") from e
        else:
            await check_res(response)
            try:
                return Response(await response.json(), response.headers)
            except aiohttp.client_exceptions.ContentTypeError as e:
                raise RuntimeError(await response.text()) from e

    async def disconnect(self):
        await self._session.close()
