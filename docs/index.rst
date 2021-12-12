Welcome to YARSAW!
===================================
YARSAW is an open source, free and easy to use API Wrapper for the `Random Stuff API`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   


===================================
Features
===================================
* Wraps all of the `Random Stuff API <https://api-info.pgamerx.com>`_
* Asynchronous
* Easy to use
* Saves you a lot of time

===================================
First Steps
===================================
1. Install the package

   .. code-block:: bash

      python3 -m pip install yarsaw

2. Register for an account at the `Random Stuff API resgistration page <https://api-info.pgamerx.com/register>`_.

3. Import the module nad create an instance of `Client <client>`

   .. code-block:: python

      import yarsaw

      client = yarsaw.Client("your_api_key")

4. Use the client to get a random joke (to get familiar with the module)

   .. code-block:: python

      import yarsaw
      import asyncio # builtin, used for asynchronous calls

      client = yarsaw.Client("your_api_key")

      async def joke():
         joke = await client.get_joke() # get the joke in form of a dict
         formatted_joke = await yarsaw.Utils().format_joke(joke) # format the joke (optional)
         print(formatted_joke) # print the joke

      asyncio.get_event_loop().run_until_complete(joke()) # run the joke() function

5. Start reading the documentation!

===================================
Clients
===================================

-----------------------------------
Client
-----------------------------------

.. autoclass:: yarsaw.Client
   :members:


===================================
Utils
===================================

Support functions for the clients.

.. autoclass:: yarsaw.Utils
   :members:
   :show-inheritance:


===================================
Data Classes
===================================

.. autoclass :: yarsaw.AIResponse
   :members:


.. autoclass :: yarsaw.GlobalCovidStats
   :members:


.. autoclass :: yarsaw.CountryCovidStats
   :members:


.. autoclass :: yarsaw.Joke
   :members:


.. autoclass :: yarsaw.Condition
   :members:

.. autoclass :: yarsaw.Country
   :members:

.. autoclass :: yarsaw.Closed
   :members:

.. autoclass :: yarsaw.Cases
   :members:

===================================
Exception Classes
===================================

.. autoclass :: yarsaw.InvalidPlanException
   :members:

.. autoclass :: yarsaw.InvalidAPIKeyException
   :members:

.. autoclass :: yarsaw.RateLimited
   :members: