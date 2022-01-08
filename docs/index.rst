Welcome to YARSAW!
======================

YARSAW is an open source, free and easy to use API Wrapper for the `Random Stuff API`_.


Features
-------------------------

* Wraps all of the `Random Stuff API <https://api-info.pgamerx.com>`_
* Async-ready
* Easy to use
* Saves you a lot of time

First Steps
-------------------------

1. Install the package

   .. code-block:: bash

      python3 -m pip install yarsaw

2. Register to get an API Key at the `Random Stuff API resgistration page <https://api-docs.pgamerx.com/Getting%20Started/register/>`_. This is used for authentication.

3. Register at `RapidAPI <https://rapidapi.com/pgamerxdev/api/random-stuff-api>`_ for a RapidAPI Key and Account, and subscribe to the Random Stuff API. This is used to make requests to the Random Stuff API and keep track of them. You can go to `The RapidAPI Developer Dashboard <https://rapidapi.com/developer/apps>`_ after logging in, select an application, head over to security, and copy its key. This is your RapidAPI Key.

4. Import the module and create an instance of `Client <client>`

   .. code-block:: python

      import yarsaw

      client = yarsaw.Client("your_rsa_api_key", "your_rapidapi_key")

5. Use the client to get a random joke (to get familiar with the module)

   .. code-block:: python

      import yarsaw
      import asyncio # builtin, used for asynchronous calls

      client = yarsaw.Client("your_api_key", "your_rapidapi_key")

      async def joke():
         joke = await client.get_joke() # get the joke in form of a dict
         formatted_joke = yarsaw.Utils().format_joke(joke) # format the joke (optional)
         print(formatted_joke) # print the joke

      asyncio.get_event_loop().run_until_complete(joke()) # run the joke() function

Now just start reading the documentation!

.. note::
   The :doc:`client` page contains all of the methods you can use to interact with the Random Stuff API, so we recommend reading that first.

.. toctree::
   :maxdepth: 1
   :caption: Pages:

   client
   utils
   faq
   changelog

Documentation Last Updated on |today|