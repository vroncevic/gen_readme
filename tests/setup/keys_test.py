# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenReadmeBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_readme.setup.keys import GenReadmeBundleKeys


class TestGenReadmeBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenReadmeBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenReadmeBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenReadmeBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenReadmeBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenReadmeBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenReadmeBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenReadmeBundleKeys.OPTION_INFO_FILE, opts)
