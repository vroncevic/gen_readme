# -*- coding: UTF-8 -*-

'''
Module
    subprocessor_test.py
Info
    Unit tests for SubProcessor adapter.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock, patch

from ats_utilities.generation.imanager import IGeneratorManager
from gen_readme.infrastructure.subprocessor import SubProcessor


class DummyLogger:

    def write_log(self, level: int, message: str) -> None:
        pass


class DummyContext:

    def __init__(self) -> None:
        self.logger = DummyLogger()


class DummyGenerator(IGeneratorManager):

    def get_context(self) -> DummyContext:
        return DummyContext()

    def generate(self, data: object) -> bool:
        return True

    def is_initialized(self) -> bool:
        return True

    def get_bundle(self) -> object:
        return None

    def update_bundle(self, bundle: object) -> None:
        pass

    def prepare_template_values(self) -> dict[str, object]:
        return {}

    def __str__(self) -> str:
        return "DummyGenerator"


class TestSubProcessor(unittest.TestCase):

    def test_init_success(self) -> None:
        generator = DummyGenerator()
        sub = SubProcessor(generator)
        self.assertEqual(sub._generator, generator)

    def test_init_errors(self) -> None:
        with self.assertRaises(Exception):
            SubProcessor(None)
        with self.assertRaises(Exception):
            SubProcessor("invalid_generator")

    @patch('gen_readme.infrastructure.subprocessor.walk')
    def test_run_success(self, mock_walk: Mock) -> None:
        mock_walk.return_value = [
            ('/tmp/out', [], ['file.txt']),
            ('/tmp/out/sub', [], ['another_file.txt'])
        ]
        generator = DummyGenerator()
        generator.generate = Mock(return_value=True)
        
        sub = SubProcessor(generator)
        params = {'output': '/tmp/out', 'name': 'test_project', 'filename': 'README.md'}
        result = sub.run(params=params)
        
        self.assertEqual(result['returncode'], 0)
        self.assertIn('success', result['stdout'])
        generator.generate.assert_called_once()

    def test_run_failure(self) -> None:
        generator = DummyGenerator()
        generator.generate = Mock(return_value=False)
        
        sub = SubProcessor(generator)
        params = {'output': '/tmp/out', 'name': 'test_project', 'filename': 'README.md'}
        result = sub.run(params=params)
        
        self.assertEqual(result['returncode'], 1)
        self.assertIn('failed', result['stderr'])

    def test_run_exception(self) -> None:
        generator = DummyGenerator()
        generator.generate = Mock(side_effect=RuntimeError('error'))
        
        sub = SubProcessor(generator)
        params = {'output': '/tmp/out', 'name': 'test_project', 'filename': 'README.md'}
        result = sub.run(params=params)
        
        self.assertEqual(result['returncode'], 1)
        self.assertIn('failed', result['stderr'])

    @patch('gen_readme.infrastructure.subprocessor.os.rename')
    @patch('gen_readme.infrastructure.subprocessor.walk')
    def test_run_rename_on_success(self, mock_walk: Mock, mock_rename: Mock) -> None:
        '''
            Tests rename behavior on run success/failure.

            :param mock_walk: Mock for walk function.
            :param mock_rename: Mock for os.rename function.
            :exceptions: None.
        '''
        mock_walk.return_value = []
        generator = DummyGenerator()
        sub = SubProcessor(generator)

        # Case 1: success = True and filename != 'README.md' -> should rename
        generator.generate = Mock(return_value=True)
        params = {
            'output': '/tmp/out',
            'filename': 'OTHER.md',
            'type': 'test_type',
            'project_name': 'test_project',
        }
        result = sub.run(params=params)
        self.assertEqual(result['returncode'], 0)
        mock_rename.assert_called_once_with('/tmp/out/README.md', '/tmp/out/OTHER.md')
        mock_rename.reset_mock()

        # Case 2: success = True and filename == 'README.md' -> should NOT rename
        params = {
            'output': '/tmp/out',
            'filename': 'README.md',
            'type': 'test_type',
            'project_name': 'test_project',
        }
        result = sub.run(params=params)
        self.assertEqual(result['returncode'], 0)
        mock_rename.assert_not_called()
        mock_rename.reset_mock()

        # Case 3: success = False and filename != 'README.md' -> should NOT rename
        generator.generate = Mock(return_value=False)
        params = {
            'output': '/tmp/out',
            'filename': 'OTHER.md',
            'type': 'test_type',
            'project_name': 'test_project',
        }
        result = sub.run(params=params)
        self.assertEqual(result['returncode'], 1)
        mock_rename.assert_not_called()

    def test_is_initialized(self) -> None:
        generator = DummyGenerator()
        generator.is_initialized = Mock(return_value=True)
        
        sub = SubProcessor(generator)
        self.assertTrue(sub.is_initialized())
        generator.is_initialized.assert_called_once()

    def test_str_representation(self) -> None:
        generator = DummyGenerator()
        sub = SubProcessor(generator)
        self.assertTrue(isinstance(str(sub), str))
