# -*- coding: utf-8 -*-

"""
shinku
~~~~~~~

A discord.py extension including useful tools for bot development and debugging.

:copyright: (c) 2025-present japandotorg
:copyright: (c) 2017-2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

# pylint: disable=wildcard-import
from shinku.cog import *  # noqa: F401, F403
from shinku.features.baseclass import Feature  # noqa: F401
from shinku.flags import Flags  # noqa: F401
from shinku.meta import *  # noqa: F401, F403

__all__ = (
    "shinku",  # noqa: F405 # type: ignore[reportUnsupportedDunderUsed]
    "Feature",
    "Flags",
    "setup",  # noqa: F405
)
