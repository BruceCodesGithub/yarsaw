import yarsaw
import asyncio  # default

client = yarsaw.Client("RSA KEY HERE", "RapidAPI KEY HERE")


async def main():
    keep_talking = True

    while keep_talking:  # Start loop
        cin = input("You:\t")

        if cin == "exit":
            keep_talking = False  # end loop
        else:
            res = await client.get_ai_response(cin, bot_name="yarsaw")
            print("Bot:\t" + res.response)

    await client.disconnect()  # disconnect the client at the end of the loop


asyncio.get_event_loop().run_until_complete(main())
