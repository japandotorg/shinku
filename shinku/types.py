# -*- coding: utf-8 -*-

"""
shinku.types
~~~~~~~~~~~~~

Declarations for type checking

:copyright: (c) 2025-present japandotorg
:copyright: (c) 2017-2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

import typing

from discord.ext import commands

BotT = typing.Union[commands.Bot, commands.AutoShardedBot]
ContextT = typing.TypeVar(
    "ContextT",
    commands.Context[commands.Bot],
    commands.Context[commands.AutoShardedBot],
)
ContextA = commands.Context[BotT]
