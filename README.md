<h2 align="center">YARSAW</h2>
<div align="center">

<a href="https://yarsaw.namantech.me/client.html"><img alt="API Coverage" src="https://img.shields.io/badge/API%20Coverage-8%2F8%20Endpoints-blue?style=for-the-badge"></a>
<a href="https://pypi.org/project/yarsaw"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/yarsaw?color=blue&style=for-the-badge"></a>
<a href="https://github.com/BruceCodesGithub/yarsaw/"><img alt="PyPI - License" src="https://img.shields.io/pypi/l/yarsaw?color=blue&style=for-the-badge"></a>
<a href="https://yarsaw.namantech.me"><img alt="Documentation Status" src='https://readthedocs.org/projects/yarsaw/badge/?version=main&style=for-the-badge'/></a>

</div>
<br>
<br>
<p align="center">YARSAW (Yet Another Random Stuff API Wrapper) is an Async, Object Oriented and Modern Python API Wrapper for the Random Stuff API. This module makes it simpler for you to interact with the API and is easy to implement into your application.</p>

Make sure to get Random Stuff API Key from [here](https://api-docs.pgamerx.com/Getting%20Started/register/) and a RapidAPI Application Key after registering and subscribing to the API [here](https://rapidapi.com/pgamerxdev/api/).

## Features

- **Tons of things you can do**
  1. Get AI Responses (useful for chatbots!)
  2. Get Anime GIFs and Waifu Images
  3. Get Animal images
  4. Get memes from various subreddits, and even create memes with pre-built templates!
  5. Get jokes and fun facts
  6. And so much more!
- **Object-oriented design**. YARSAW takes inspiration from [randomstuff.py](https://github.com/nerdguyahmad/randomstuff.py) and sends you the data from the API in form of objects instead of plain JSON.
- **Async-ready**. YARSAW provides an async client for async enviorments using aiohttp.
- **Easy to use**. YARSAW is well-documented, and has utility features to help you with your requests.
- **Saves your time**. i) No need to learn about the API itself and its complicated design. ii) No need to enter the credentials again and again. Enter it once, and get coding. YARSAW will take care of the boring stuff for you. iii) No need to handle the unhelpful errors given by requests/aiohttp/RapidAPI. Get human-headable, descriptive and helpful error messages. iv) Common errors and issues are prevented and declared before runtime.

## Examples

```py
import yarsaw
import asyncio
client = yarsaw.Client("RSA Key", "RapidAPI Key")
async def joke():
   joke = await client.get_joke() # get the joke
   formatted_joke = yarsaw.format_joke(joke) # format the joke (optional)
   print(formatted_joke) # print the joke
asyncio.get_event_loop().run_until_complete(joke()) # run the joke() function
```

## Installation

```bash
python3 -m pip install -U yarsaw
```

## Useful Links

- [**Documentation**](https://yarsaw.namantech.me/)
- [**Random Stuff API**](https://rapidapi.com/pgamerxdev/api/random-stuff-api/)
- [**Random Stuff API Discord**](https://discord.gg/GpYTdHaNhe)
