# -*- coding: utf-8 -*-

"""
shinku subclassing test 2
~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a valid extension file for discord.py intended to
discover weird behaviors related to subclassing.

This variant overrides behavior directly.

:copyright: (c) 2025-present japandotorg
:copyright: (c) 2017-2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

from discord.ext import commands

import shinku
from shinku.types import ContextT


class Magnet2(*shinku.OPTIONAL_FEATURES, *shinku.STANDARD_FEATURES): # type: ignore[reportUntypedBaseClass]  # pylint: disable=too-few-public-methods
    """
    The extended Sinku cog
    """

    @shinku.Feature.Command(name="shinku", aliases=["shin"], invoke_without_command=True, ignore_extra=False)
    async def shin(self, ctx: ContextT):
        """
        override test
        """
        return await ctx.send("The behavior of this command has been overridden directly.")


async def setup(bot: commands.Bot):
    """
    The setup function for the extended cog
    """

    await bot.add_cog(Magnet2(bot=bot))
