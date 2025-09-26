import aiohttp


class FavoritesAPIClient:
    def __init__(self, base_url: str = "https://regions-test.2gis.com"):
        self.base_url = base_url
        self.session = None
        self.token = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *args):
        await self.session.close()

    async def authenticate(self):
        async with self.session.post(f"{self.base_url}/v1/auth/tokens") as response:
            if response.status == 200 and 'token' in response.cookies:
                self.token = response.cookies['token'].value
                return True
        return False

    async def create_favorite(self, data, use_auth: bool = True):
        cookies = {"token": self.token} if use_auth and self.token else {}

        async with self.session.post(
                f"{self.base_url}/v1/favorites",
                data=data,
                cookies=cookies
        ) as response:
            response_data = await response.json() if response.content_length else {}
            return response.status, response_data