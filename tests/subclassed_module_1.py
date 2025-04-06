# -*- coding: utf-8 -*-

"""
shinku subclassing test 1
~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a valid extension file for discord.py intended to
discover weird behaviors related to subclassing.

This variant overrides behavior using a Feature.

:copyright: (c) 2025-present japandotorg
:copyright: (c) 2017-2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

from discord.ext import commands

import shinku
from shinku.types import ContextT


class ThirdPartyFeature(shinku.Feature):
    """
    overriding feature for test
    """

    @shinku.Feature.Command(name="shinku", aliases=["jsk"], invoke_without_command=True, ignore_extra=False)
    async def jsk(self, ctx: ContextT):
        """
        override test
        """
        return await ctx.send("The behavior of this command has been overridden with a third party feature.")


class Magnet1(ThirdPartyFeature, *shinku.OPTIONAL_FEATURES, *shinku.STANDARD_FEATURES):  # pylint: disable=too-few-public-methods
    """
    The extended Sinku cog
    """


async def setup(bot: commands.Bot):
    """
    The setup function for the extended cog
    """

    await bot.add_cog(Magnet1(bot=bot))
