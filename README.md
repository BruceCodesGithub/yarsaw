<h2 align="center">YARSAW</h2>
<div align="center">
<img src="https://img.shields.io/pypi/v/yarsaw">  

<img alt="PyPI - License" src="https://img.shields.io/pypi/l/yarsaw">

<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/yarsaw?color=blue">

<img src='https://readthedocs.org/projects/yarsaw/badge/?version=latest' alt='Documentation Status' />

</div>
<br>
<br>
<p align="center">YARSAW (Yet Another Random Stuff API Wrapper) is an Async, Object Oriented and Modern Python API Wrapper for the Random Stuff API. This module makes it simpler for you to interact with the API and is easy to implement into your application.</p>


**Make sure to get an API Key from [here](https://api-info.pgamerx.com/register.html) before trying to access this module.**

## Features

- Async and fast
- Object oriented design (Raw outputs are also available)
- Tons of thigs you can do
    - Get AI Responses (useful for making chatbots)
    - Get Covid/Weather stats
    - Edit images into memes
    - Gets facts, jokes, images (including aww, meme, etc.)
- Simple and easy
- No need to learn about the Random Stuff API. Just get started with your project
- Saves time

## Examples

```py
import yarsaw
import asyncio
client = yarsaw.Client("your_api_key")
async def joke():
   joke = await client.get_joke() # get the joke
   formatted_joke = await yarsaw.Utils().format_joke(joke) # format the joke (optional)
   print(formatted_joke) # print the joke
asyncio.get_event_loop().run_until_complete(joke()) # run the joke() function
```

## Installation

```bash
python3 -m pip install yarsaw
```

## Changes

### `1.3`
(stable)

- The `Client` class now returns objects which are easier to work with.
- `RawClient` class can be used ot return the raw JSON response from the API.

### `1.2`
(stable)

- Updated Docs - now view it [here](https://yarsaw.namantech.me/)
    - Uses ReadTheDocs.
    - Uses Sphinx instead of MKDocs
    - Updated the docs to be more readable.
    - Is updated automatically with docstrings.
    - Covers all the methods. Fixed minor mistakes.
- Created a `Utils` class, added `format_joke()` and `generate_uid()` to the `Utils`.
- Added docstrings to all the methods.
- Better code style.
- Updated many other things.

### `1.0`

(stable)
- Updated docs
- Renamed functions in `Client()`
    - `ai` -> `get_ai_response()`
    - `joke` -> `get_joke()`
    - `fact` -> `get_fact()`
    - `waifu` -> `get_waifu()`
    - `image` -> `get_image()`
    - `covid` -> `get_covid_stats()`
    - `weather` -> `get_weather()`

- Added new function `generate_uid()`
- Many more changes


## Documentation

[Read the Documention here](https://yarsaw.namantech.me/)