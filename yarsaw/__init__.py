"""
YARSAW
~~~~~~~~~~~~~~

An API Wrapper for the Random Stuff API.

:copyright: 2021-present BruceCodesGithub.
:licence: MIT. See LICENSE for more details.
"""

from .client import *
from .utils import *
from .exceptions import *

__title__ = "yarsaw"
__summary__ = "An async wrapper for Random Stuff API"
__author__ = "Bruce"
__version__ = "2.1.0"
__license__ = "MIT"
__copyright__ = "2021-present BruceCodesGithub"


def get_version():
    return __version__
