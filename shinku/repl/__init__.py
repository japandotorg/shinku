# -*- coding: utf-8 -*-

"""
shinku.repl
~~~~~~~~~~~~

Repl-related operations and tools for Sinku.

:copyright: (c) 2025-present japandotorg
:copyright: (c) 2017-2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

# pylint: disable=wildcard-import
from shinku.repl.compilation import *  # noqa: F401, F403
from shinku.repl.disassembly import create_tree, disassemble, get_adaptive_spans  # type: ignore[reportUnusedImport]  # noqa: F401
from shinku.repl.inspections import all_inspections  # type: ignore[reportUnusedImport]  # noqa: F401
from shinku.repl.repl_builtins import get_var_dict_from_ctx  # type: ignore[reportUnusedImport]  # noqa: F401
from shinku.repl.scope import *  # noqa: F401, F403
