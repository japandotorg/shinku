# -*- coding: utf-8 -*-

"""
shinku.meta
~~~~~~~~~~~~

Meta information about shinku.

:copyright: (c) 2025-present japandotorg
:copyright: (c) 2017-2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

import typing

__all__ = (
    "__author__",
    "__copyright__",
    "__docformat__",
    "__license__",
    "__title__",
    "__version__",
    "version_info",
)


class VersionInfo(typing.NamedTuple):
    """Version info named tuple for Sinku"""

    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int


version_info = VersionInfo(major=2, minor=6, micro=0, releaselevel="final", serial=0)

__author__ = "japandotorg"
__copyright__ = "Copyright 2025-present japandotorg"
__docformat__ = "restructuredtext en"
__license__ = "MIT"
__title__ = "shinku"
__version__ = ".".join(
    map(str, (version_info.major, version_info.minor, version_info.micro))
)
