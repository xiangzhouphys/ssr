#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ssr` package."""

# Third party modules
import pytest

# First party modules
import ssr


def test_version():
    assert ssr.__version__.count(".") == 2


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
