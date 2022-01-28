<h2 align="center">YARSAW</h2>
<div align="center">
    
<img alt="PyPi - Version" src="https://img.shields.io/pypi/v/yarsaw?color=blue&style=flat-square">  
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/yarsaw?color=blue&style=flat-square">
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/yarsaw?color=blue&style=flat-square">
<img alt="Documentation Status" src='https://readthedocs.org/projects/yarsaw/badge/?version=main'/>

</div>
<br>
<br>
<p align="center">YARSAW (Yet Another Random Stuff API Wrapper) is an Async, Object Oriented and Modern Python API Wrapper for the Random Stuff API. This module makes it simpler for you to interact with the API and is easy to implement into your application.</p>


Make sure to get Random Stuff API Key from [here](https://api-docs.pgamerx.com/Getting%20Started/register/) and a RapidAPI Application Key after registering and subscribing to the API [here](https://rapidapi.com/pgamerxdev/api/).


## Features

- Loads of things you can do
    1. Get AI Responses (useful for creating chatbots)
    1. Get Animal Images (Dogs, Cats, Wolfs and Foxes)
    1. Get Anime GIFs (`happy`, `hi`, `hug`, `punch`, `pat`, and more)
    1. Create memes with pre-built templates
    1. Get jokes (`any`, `dark`, `pun`, `spooky`, `christmas`, `programming`, `misc`)
    1. Fetch Reddit posts and memes
    1. Get weather data for any city
    1. Get fun facts (`all`, `emoji`, `dog`, `cat`, `food`, `space`, `covid`, `computer`)
    1. Get waifu images (over 32 different types!)
- Fast and asynchronous
- Object oriented design
- Easy to use
- Well documented
- Wraps the full API
- Kept up-to-date
- Utility functions to help you with your requests
- Saves your time
    - No need to learn about the API itself and its complex design
    - No need to enter your API Keys multiple times
    - No need to handle the complex and unhelpful errors given by requests/aiohttp or RapidAPI. Get human-readable and helpful errors instead. Common errors are prevented before runtime.

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

## Links

- [**Documentation**](https://yarsaw.namantech.me/)
- [**Random Stuff API**](https://rapidapi.com/pgamerxdev/api/random-stuff-api/)
- [**Random Stuff API Discord**](https://discord.gg/GpYTdHaNhe)

## Changes

[View Full Changelog](https://yarsaw.namantech.me/changelog.html)

#### 2.0.1

- Added support for `/weather`
- Parameter `base` was removed from class `Client`
- Error handling for incorrect API keys was improved

#### 2.0

This is a major change. The Random Stuff API was completely rewritten, and so was this module. Aside from new functions,

- Docs were updated
    - Uses the ReadTheDocs theme for documentation
    - The documentation is no longer a single page, but a collection of pages.
- Since the API now has more use of headers than ever (it returns the number of daily requests left), all methods return headers along with other data.
- The ``generate_uid`` and ``format_joke`` methods are no longer async - them being async was useless.
- New Docstrings and comments
- ``RawClient`` was terminated.
- A lot more updates

