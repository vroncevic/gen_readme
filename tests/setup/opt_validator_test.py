# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenReadmeBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_readme.setup.opt_validator import GenReadmeBundleOptionsValidator


class TestGenReadmeBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenReadmeBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenReadmeBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenReadmeBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenReadmeBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenReadmeBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenReadmeBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenReadmeBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenReadmeBundleOptionsValidator.is_valid({'info_file': 123}))
