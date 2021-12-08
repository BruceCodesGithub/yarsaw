import yarsaw
import os
import asyncio
import dotenv

dotenv.load_dotenv()

client = yarsaw.Client(os.getenv("API_KEY"))


async def main():
    joke = await client.get_joke(joke_type="dark")
    safe_joke = await client.get_safe_joke()
    formatted_safe_joke = await yarsaw.Utils().format_joke(
        safe_joke, format_as="{setup} ... {delivery}"
    )
    print(joke, formatted_safe_joke)
    await client.disconnect()


asyncio.get_event_loop().run_until_complete(main())
