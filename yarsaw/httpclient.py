import aiohttp
from .utils import check_res

class HTTPClient:
    def __init__(self, authorization: str):
        self._key = authorization
        self._base = "https://api.pgamerx.com/v5"
        self._session = aiohttp.ClientSession()

    async def request(self, endpoint, *, params=None):
        if params is None:
            params = {}
        
        async with self._session.get(
            f"{self._base}/{endpoint}",
            headers={"Authorization": self._key},
            params=params,
        ) as response:

            await check_res(response)
            await self._session.close()
            try:
                return await response.json()
            except aiohttp.client_exceptions.ContentTypeError:
                return await response.text()
