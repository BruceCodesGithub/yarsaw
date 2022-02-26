################################
Changelog
################################


*************
``2.1``
*************

* Documentation update.
    * Change theme to ``furo``.
* Edit dataclasses.
    * Dataclasses now have more pythonic parameters for ease of use.
    * Replaced ``headers`` with ``APIInfo``.
* Most methods now return dataclass objects.
* Remove nested return type from ``get_animal_image()`` and ``get_anime_gif()``
* Various changes.

*************
``2.0.1``
*************

* Added support for ``/weather``
* Parameter ``base`` was removed from class ``Client``
* Error handling for incorrect API keys was improved

*************
``2.0``
*************

This is a major change. The Random Stuff API was completely rewritten, and so was this module. Aside from new functions,

* Docs were updated
    * Uses the ReadTheDocs theme for documentation
    * The documentation is no longer a single page, but a collection of pages.
* Since the API now has more use of headers than ever (it returns the number of daily requests left), all methods return headers along with other data.
* The ``generate_uid`` and ``format_joke`` methods are no longer async - them being async was useless.
* New Docstrings and comments
* ``RawClient`` was terminated.
* A lot more updates

*************
``1.3``
*************

* The ``Client`` class now returns objects which are easier to work with.
* ``RawClient`` class can be used to return the raw JSON response from the API.

*************
``1.2``
*************

* Updated Docs
    * Uses ReadTheDocs.
    * Uses Sphinx instead of MKDocs
    * More readable.
    * Is updated automatically with docstrings.
    * Covers all the methods. Fixed minor mistakes.
* Created a ``Utils`` class, added ``format_joke()`` and ``generate_uid()`` to the Utils.
* Added docstrings to all the methods.
* Better code style (black).
* Updated many other things.

*************
``1.0``
*************

* Updated docs
* Renamed functions in ``Client``
* Added new function ``generate_uid()``
* Many more bug fixes and changes.