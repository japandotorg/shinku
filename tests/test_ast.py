# -*- coding: utf-8 -*-

"""
shinku ast tree generation test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:copyright: (c) 2025-present japandotorg
:copyright: (c) 2017-2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

import inspect

from shinku.repl.disassembly import create_tree


def test_ast_missing_fields():
    # should not raise
    create_tree(inspect.cleandoc("""
        def h(*, a):
            print(a)
    """), use_ansi=False)
