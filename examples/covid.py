import yarsaw
import os
import asyncio
import dotenv

dotenv.load_dotenv()

client = yarsaw.Client(os.getenv("API_KEY"))


async def main():
    global_stats = await client.get_covid_stats()
    print(
        global_stats,
        global_stats.total_cases,
        global_stats.total_deaths,
        global_stats.total_recovered,
    )
    us_stats = await client.get_covid_stats(country="US")
    print(
        us_stats,
        us_stats.cases.total,
        us_stats.cases.deaths,
        us_stats.cases.recovered,
    )
    await client.disconnect()


asyncio.get_event_loop().run_until_complete(main())
