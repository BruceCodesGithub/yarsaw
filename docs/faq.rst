****************************
Frequently Asked Questions
****************************

-------------------
How do I use this?
-------------------
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

--------------------------------------------
Why does Random Stuff API Require two keys?
--------------------------------------------
The developer of the Random Stuff API decided to switch to the RapidAPI servers because they are more reliable and faster. The RapidAPI servers require a RapidAPI Key and an Account. The Random API key is used for authentication and the RapidAPI key is used to make requests to the Random Stuff API. Now, several issues were fixed, such as:

* Premium plans were only applicable to the premium endpoints. This meant that even if you had bought premium, you will still only be able to post x requests to the free endpoints instead of xxx requests.
* The API had bad error messages.
* The API was slow.
* The API did not have many examples available.

------------------------------
Does this wrapper still work?
------------------------------
YES! Unlike most other wrappers, YARSAW still works! Although the API was shifted to RapidAPI and had tons of changes, the wrapper was updated accordingly to accomodate the changes.

---------------
I have an issue
---------------
If its an issue with the wrapper, please open an issue at `GitHub <https://github.com/BruceCodesGithub/yarsaw/issues>`_. If there's a question about the API itself, please join `the PGamerX Studio Discord Server <https://discord.gg/wWgjpK9MDv>`_ and ask there.

----------------------------
Who is behind this wrapper?
----------------------------
YARSAW is developed by `BruceDev <https://github.com/BruceCodesGithub>`_.
The API itself is developed by `PGamerX <https://pgamerx.com>`_.

Documentation Last Updated on |today|