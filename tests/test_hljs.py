# -*- coding: utf-8 -*-

"""
shinku.hljs test
~~~~~~~~~~~~~~~~~

:copyright: (c) 2025-present japandotorg
:copyright: (c) 2017-2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

import pytest

from shinku.hljs import get_language


@pytest.mark.parametrize(
    ("filename", "language"),
    [
        ('base.py', 'py'),
        ('config.yml', 'yml'),
        ('requirements.txt', ''),
        ('#!/usr/bin/env python', 'python'),
        ('#!/usr/bin/unknown', '')
    ]
)
def test_hljs(filename: str, language: str):
    assert get_language(filename) == language
