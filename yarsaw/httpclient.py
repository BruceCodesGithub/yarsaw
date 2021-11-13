import aiohttp
from .utils import check_res


class HTTPClient:
    def __init__(self, authorization: str):
        self.__key = authorization
        self._base = "https://api.pgamerx.com/v5"
        self._session = aiohttp.ClientSession()

    async def request(self, endpoint, *, params=None):
        if params is None:
            params = {}

        async with self._session.get(
            f"{self._base}/{endpoint}",
            headers={"Authorization": self.__key},
            params=params,
        ) as response:

            await check_res(response)
            try:
                return await response.json()
            except aiohttp.client_exceptions.ContentTypeError:
                return await response.text()

    async def close(self):
        await self._session.close()
