import yarsaw
import os
import asyncio
import dotenv

dotenv.load_dotenv()

client = yarsaw.Client(os.getenv("API_KEY"))


async def main():
    message = input("You:\t")
    while message != "quit":
        res = await client.get_ai_response(message)
        print(f"Bot:\t{res.response}")
        message = input("You:\t")
    await client.disconnect()


asyncio.get_event_loop().run_until_complete(main())
