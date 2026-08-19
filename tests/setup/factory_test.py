# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenReadmeBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_readme.setup.bundle import GenReadmeBundle
from gen_readme.setup.factory import GenReadmeBundleFactory


class TestGenReadmeBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenReadmeBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenReadmeBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_readme/infrastructure/config/gen_readme.cfg'}
        bundle = GenReadmeBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenReadmeBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenReadmeBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenReadmeBundleFactory.get_version(), '1.1.8')
