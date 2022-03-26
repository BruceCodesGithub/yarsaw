import unittest
import yarsaw
import os
import dotenv
import asyncio

dotenv.load_dotenv()

client = yarsaw.Client(os.getenv("RSA_KEY"), os.getenv("APP_KEY"))


class TestEndpoints(unittest.TestCase):
    async def ai(self):
        res = await client.get_ai_response("Hello")
        self.assertIsInstance(res, yarsaw.AIResponse)

    async def animal(self):
        res = await client.get_animal_image("Fox")
        self.assertIsInstance(res, yarsaw.AnimalImage)

    async def anime(self):
        res = await client.get_anime_gif("happy", 1)
        self.assertIsInstance(res, list[yarsaw.AnimeGIF])

    async def canvas(self):
        res = await client.canvas("changemymind", txt="YARSAW is Awesome!")
        self.assertIsInstance(res, yarsaw.CanvasResponse)

    async def joke(self):
        res = await client.get_joke()
        self.assertIsInstance(res, yarsaw.Joke)

    async def fetch_subreddit_post(self):
        res = await client.fetch_subreddit_post("aww")
        self.assertIsInstance(res, yarsaw.RedditPost)

    async def fetch_post(self):
        res = await client.fetch_post("aww")
        self.assertIsInstance(res, yarsaw.RedditPost)

    async def fetch_post_by_id(self):
        res = await client.fetch_post_by_id("awyf90")
        self.assertIsInstance(res, yarsaw.RedditPost)

    async def fetch_random_post(self):
        res = await client.fetch_random_post()
        self.assertIsInstance(res, yarsaw.RedditPost)

    async def random_meme(self):
        res = await client.random_meme()
        self.assertIsInstance(res, yarsaw.RedditPost)

    async def get_weather(self):
        res = await client.get_weather("New York")
        self.assertIsInstance(res, dict)

    async def get_fact(self):
        res = await client.get_fact()
        self.assertIsInstance(res, yarsaw.Fact)

    def test_ai(self):
        asyncio.get_event_loop().run_until_complete(self.ai())

    def test_animal(self):
        asyncio.get_event_loop().run_until_complete(self.animal())

    def test_anime(self):
        asyncio.get_event_loop().run_until_complete(self.anime())

    def test_canvas(self):
        asyncio.get_event_loop().run_until_complete(self.canvas())

    def test_joke(self):
        asyncio.get_event_loop().run_until_complete(self.joke())

    def test_weather(self):
        asyncio.get_event_loop().run_until_complete(self.get_weather())

    def test_reddit(self):
        asyncio.get_event_loop().run_until_complete(self.fetch_subreddit_post())
        asyncio.get_event_loop().run_until_complete(self.fetch_post())
        asyncio.get_event_loop().run_until_complete(self.fetch_post_by_id())
        asyncio.get_event_loop().run_until_complete(self.fetch_random_post())
        asyncio.get_event_loop().run_until_complete(self.random_meme())

    def test_fact(self):
        asyncio.get_event_loop().run_until_complete(self.get_fact())


if __name__ == "__main__":
    unittest.main()
