# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
Info
    Unit tests for GenReadmeBundleRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_readme.core.service.iservice import IService
from gen_readme.core.service.isubprocessor import ISubProcessor
from gen_readme.infrastructure.cli.icli import ICLI
from gen_readme.setup.bundle import GenReadmeBundle
from gen_readme.setup.registry import GenReadmeBundleRegistry


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


class TestGenReadmeBundleRegistry(unittest.TestCase):

    def test_create_bundle_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        dependencies = {
            'base': mock_base,
            'service': dummy_service,
            'subprocessor': dummy_subprocessor,
            'cli': dummy_cli
        }
        
        bundle = GenReadmeBundleRegistry.create_bundle(dependencies)
        self.assertIsInstance(bundle, GenReadmeBundle)
        self.assertEqual(bundle.base, mock_base)

    def test_create_bundle_invalid_dependencies(self) -> None:
        with self.assertRaises(Exception):
            GenReadmeBundleRegistry.create_bundle(None)

    def test_get_version(self) -> None:
        self.assertEqual(GenReadmeBundleRegistry.get_version(), '1.1.8')
