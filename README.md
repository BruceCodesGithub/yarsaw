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


--Make sure to get Random Stuff API Key from [here](https://api-docs.pgamerx.com/Getting%20Started/register/) and RapidAPI Key after registering and subscribing to the API [here](https://rapidapi.com/pgamerxdev/api/)random-stuff-api).


## Features

- Async and fast
- Object oriented design (Raw outputs are also available)
- Tons of thigs you can do
    - Get AI Responses (useful for making chatbots)
    - Edit images into memes
    - Gets facts, jokes, images (including aww, meme, etc.)
    - Gets reddit posts - random memes, random posts from subreddits, etc.
- Simple and easy
- No need to learn about the Random Stuff API. Just get started with your project
- Saves time

## Examples

```py
import yarsaw
import asyncio
client = yarsaw.Client("RSA Key", "RapidAPI Key")
async def joke():
   joke = await client.get_joke() # get the joke
   formatted_joke = yarsaw.Utils().format_joke(joke) # format the joke (optional)
   print(formatted_joke) # print the joke
asyncio.get_event_loop().run_until_complete(joke()) # run the joke() function
```

## Installation

```bash
python3 -m pip install yarsaw
```

## Changes

(2.0)

This is a major change. The Random Stuff API was completely rewritten, and so was this module. Aside from new functions,

- Docs were updated
    - Uses the ReadTheDocs theme for documentation
    - The documentation is no longer a single page, but a collection of pages.
- Since the API now has more use of headers than ever (it returns the number of daily requests left), all methods return headers along with other data.
- The ``generate_uid`` and ``format_joke`` methods are no longer async - them being async was useless.
- New Docstrings and comments
- A lot more updates

## Documentation

[Read the Documention here](https://yarsaw.namantech.me/)