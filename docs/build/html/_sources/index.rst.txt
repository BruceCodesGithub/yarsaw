.. The Official YARSAW Docs

Welcome to YARSAW!
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

YARSAW (Yet Another Random Stuff API Wrapper) is an async API wrapper for the `Random Stuff API`_. This module makes it easier for you to interact with the API and solves all your needs.

===============
Why YARSAW?
===============

**Without YARSAW**

.. code-block :: python

   async with aiohttp.ClientSession() as session:
      async with session.get('https://api.pgamerx.com/v5/joke', params={'type' : 'any'}, headers={'Authorization':'API KEY'}) as response:
         if response['type'] == 'twopart': # format the joke manually
            print(response['setup'], '\n', response['delivery'])
         else:
            print(response['joke'])

**With YARSAW**

.. code-block :: python

   client = yarsaw.Client('[YOUR API HEY HERE]') # need to pass the API Key ONCE and for all!
   joke = await client.get_joke(joke_type='any') # simpler customization
   print(await yarsaw.Utils().format_joke(joke)) # format the joke automatically!


===============
Getting Started
===============

1. **Install YARSAW**

.. code-block :: bash

   python3 -m pip install yarsaw

2. Get your API Key from `The Official Website's registration page`_.

3. Get a quick idea of how YARSAW works

.. code-block :: python

   import yarsaw # Import the module
   import asyncio # Default Module


   client = yarsaw.Client("[PASTE YOUR API KEY HERE]")

   async def main():
      print(await client.joke())

   asyncio.get_event_loop().run_until_complete(main())

4. Start Reading the Docs

.. _Random Stuff API: https://api-info.pgamerx.com
.. _The OfficiaL Website's registration page: https://api-info.pgamerx.com/register