import aiohttp
from .utils import check_res
from dataclasses import dataclass


@dataclass(frozen=True)
class Response:
    body: dict
    headers: dict


class HTTPClient:
    def __init__(
        self,
        authorization: str,
        key,
        *,
        base: str = "https://random-stuff-api.p.rapidapi.com",
    ):
        self.__auth = authorization
        self.__key = key
        self._base = base
        self._session = aiohttp.ClientSession()

    async def request(self, endpoint, *, params=None):
        if params is None:
            params = {}

        async with self._session.get(
            f"{self._base}/{endpoint}",
            headers={
                "Authorization": self.__auth,
                "X-RapidAPI-Key": self.__key,
                "X-RapidAPI-Host": "random-stuff-api.p.rapidapi.com",
            },
            params=params,
        ) as response:

            await check_res(response)
            try:
                return Response(await response.json(), response.headers)
            except aiohttp.client_exceptions.ContentTypeError:
                raise RuntimeError(await response.text())

    async def disconnect(self):
        await self._session.close()
