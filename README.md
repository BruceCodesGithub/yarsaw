# Yet Another Random Stuff API Wrapper - YARSAW

YARSAW is an Async Python API Wrapper for the [Random Stuff API](https://api-info.pgamerx.com). This module makes it simpler for you to interact with the API and is easy to implement into your application.

**Make sure to get an API Key from [here](https://api-info.pgamerx.com/register.html) before trying to access this module.**

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

## Contributing 
To contribute, fork the [Official Repository](https://github.com/BruceCodesGithub/yarsaw/) and make a pull request.
