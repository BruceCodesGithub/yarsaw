import aiohttp
from .utils import check_res

class HTTPClient:
    def __init__(self, authorization: str):
        self.__key__ = authorization
        self.__base__ = "https://api.pgamerx.com/v5"

    async def request(self, endpoint, *, params=None):
        if params is None:
            params = {}
        session = aiohttp.ClientSession()
        async with session.get(
            f"{self.__base__}/{endpoint}",
            headers={"Authorization": self.__key__},
            params=params,
        ) as response:

            await check_res(response)
            await session.close()
            try:
                return await response.json()
            except aiohttp.client_exceptions.ContentTypeError:
                return await response.text()
