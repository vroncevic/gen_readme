# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
Info
    Unit tests for GenReadmeBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_readme.core.service.iservice import IService
from gen_readme.core.service.isubprocessor import ISubProcessor
from gen_readme.infrastructure.cli.icli import ICLI
from gen_readme.setup.bundle import GenReadmeBundle
from gen_readme.setup.validator import GenReadmeBundleValidator


class DummyService:

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True


class DummySubProcessor:

    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class DummyCLI:

    def run(self) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class TestGenReadmeBundleValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenReadmeBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        GenReadmeBundleValidator.validate(bundle)

    def test_validate_bundle_none(self) -> None:
        with self.assertRaises(Exception):
            GenReadmeBundleValidator.validate(None)

    def test_validate_bundle_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenReadmeBundleValidator.validate("invalid_bundle")

    def test_validate_missing_components(self) -> None:
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        with self.assertRaises(Exception):
            bundle = GenReadmeBundle(
                base=None,
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenReadmeBundleValidator.validate(bundle)

    def test_validate_invalid_component_types(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        with self.assertRaises(Exception):
            bundle = GenReadmeBundle(
                base="invalid",
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenReadmeBundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenReadmeBundle(
                base=mock_base,
                service="invalid",
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenReadmeBundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenReadmeBundle(
                base=mock_base,
                service=dummy_service,
                subprocessor="invalid",
                cli=dummy_cli
            )
            GenReadmeBundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenReadmeBundle(
                base=mock_base,
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli="invalid"
            )
            GenReadmeBundleValidator.validate(bundle)

    def test_is_valid_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenReadmeBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )
        self.assertTrue(GenReadmeBundleValidator.is_valid(bundle))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenReadmeBundleValidator.is_valid(None))
        self.assertFalse(GenReadmeBundleValidator.is_valid("invalid"))
