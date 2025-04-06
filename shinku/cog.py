# -*- coding: utf-8 -*-

"""
shinku.cog
~~~~~~~~~~~~

The Sinku debugging and diagnostics cog implementation.

:copyright: (c) 2025-present japandotorg
:copyright: (c) 2017-2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

import inspect
import typing

from discord.ext import commands

from shinku.features.baseclass import Feature
from shinku.features.filesystem import FilesystemFeature
from shinku.features.guild import GuildFeature
from shinku.features.invocation import InvocationFeature
from shinku.features.management import ManagementFeature
from shinku.features.python import PythonFeature
from shinku.features.root_command import RootCommand
from shinku.features.shell import ShellFeature
from shinku.features.sql import SQLFeature
from shinku.features.voice import VoiceFeature

__all__ = (
    "Sinku",
    "STANDARD_FEATURES",
    "OPTIONAL_FEATURES",
    "setup",
)

STANDARD_FEATURES = (
    VoiceFeature,
    GuildFeature,
    FilesystemFeature,
    InvocationFeature,
    ShellFeature,
    SQLFeature,
    PythonFeature,
    ManagementFeature,
    RootCommand,
)

OPTIONAL_FEATURES: typing.List[typing.Type[Feature]] = []

try:
    from shinku.features.youtube import YouTubeFeature
except ImportError:
    pass
else:
    OPTIONAL_FEATURES.insert(0, YouTubeFeature)


class Sinku(*OPTIONAL_FEATURES, *STANDARD_FEATURES):  # type: ignore[reportUntypedBaseClass]  # pylint: disable=too-few-public-methods
    """
    The frontend subclass that mixes in to form the final Sinku cog.
    """


async def async_setup(bot: commands.Bot):
    """
    The async setup function defining the shinku.cog and shinku extensions.
    """

    await bot.add_cog(Sinku(bot=bot))


def setup(bot: commands.Bot):  # pylint: disable=inconsistent-return-statements
    """
    The setup function defining the shinku.cog and shinku extensions.
    """

    if inspect.iscoroutinefunction(bot.add_cog):
        return async_setup(bot)

    bot.add_cog(Sinku(bot=bot))  # type: ignore[reportUnusedCoroutine]
