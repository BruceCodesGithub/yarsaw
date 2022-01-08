"""
YARSAW
~~~~~~~~~~~~~~
An async wrapper for the Random Stuff API.

:copyright: 2021-present BruceCodesGithub.
:licence: MIT. See LICENSE for more details.
"""

# from .clients import *
from .clients import *
from .utils import *
from .data_classes import *
from .exceptions import *

__title__ = "yarsaw"
__summary__ = "An async wrapper for Random Stuff API"
__author__ = "Bruce"
__version__ = "1.3"
__license__ = "MIT"
__copyright__ = "2021-present BruceCodesGithub"


def get_version():
    return __version__
