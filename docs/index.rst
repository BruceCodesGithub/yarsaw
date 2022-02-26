######################
**Welcome to YARSAW!**
######################

YARSAW is an open source, free and easy to use API Wrapper for the `Random Stuff API`_.


***************
Overview
***************

Features:

* Wraps all of the `Random Stuff API <https://api-info.pgamerx.com>`_
* Async-ready
* Easy to use
* Saves you a lot of time

*****************
Installation
*****************

To install the latest stable version of YARSAW, run the following command:

.. code-block:: bash

      python -m pip install yarsaw

To install a specific version of YARSAW, run the following command:

.. code-block:: bash

      python -m pip install yarsaw==<version>

To install the beta version of YARSAW, run the following command:

.. code-block:: bash

      python -m pip install git+https://github.com/BruceCodesGithub/yarsaw --upgrade



****************
Getting Started
****************

Get your API Keys
==================

1. Register to get an API Key at the `Random Stuff API resgistration page <https://api-docs.pgamerx.com/Getting%20Started/register/>`_. This is used for authentication.

2. Register at `RapidAPI <https://rapidapi.com/pgamerxdev/api/random-stuff-api>`_ for a RapidAPI Key and Account, and subscribe to the Random Stuff API. This is used to make requests to the Random Stuff API and keep track of them. You can go to `The RapidAPI Developer Dashboard <https://rapidapi.com/developer/apps>`_ after logging in, select an application, head over to security, and copy its key. This is your RapidAPI Key.

Examples
========

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

****************
Contents
****************

.. tip::
   The :doc:`client` page contains all of the methods you can use to interact with the Random Stuff API, so we recommend reading that first.

.. toctree::
   :maxdepth: 1
   :caption: Documentation

   client
   utils
   
.. toctree::
   :maxdepth: 1
   :caption: Other Pages and Resources

   faq
   changelog

Documentation Last Updated on |today|