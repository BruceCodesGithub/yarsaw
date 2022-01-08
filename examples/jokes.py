import yarsaw
import asyncio  # default

client = yarsaw.Client("RSA KEY HERE", "RapidAPI KEY HERE")


async def main():
    joke = await client.get_joke()  # get joke as a Joke object
    safe_joke = await client.get_safe_joke()  # get a SFW joke as a Joke object
    print(yarsaw.Utils().format_joke(joke))  # format the joke
    print(
        yarsaw.Utils().format_joke(safe_joke, format_as="{setup} ... {punchline}")
    )  # format the safe joke

    await client.disconnect()  # disconnect the client at the end of the process


asyncio.get_event_loop().run_until_complete(main())
