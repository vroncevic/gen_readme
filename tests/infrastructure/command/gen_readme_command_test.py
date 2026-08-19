# -*- coding: UTF-8 -*-

'''
Module
    gen_readme_command_test.py
Info
    Unit tests for GenReadmeCommandDefinition and GenReadmeCommandExecutor.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from gen_readme.core.service.iservice import IService
from gen_readme.infrastructure.command.gen_readme_command_definition import GenReadmeCommandDefinition
from gen_readme.infrastructure.command.gen_readme_command_executor import GenReadmeCommandExecutor


class TestGenReadmeCommand(unittest.TestCase):

    def test_definition(self) -> None:
        definition = GenReadmeCommandDefinition()
        self.assertEqual(definition.name, 'generate-readme')
        self.assertEqual(definition.help_text, 'Generate README.md file')
        self.assertEqual(len(definition.options), 10)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success(self) -> None:
        definition = GenReadmeCommandDefinition()
        executor = GenReadmeCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}
        
        params = {'name': 'test', 'output': '.'}
        result = executor.execute(params=params, service=mock_service)
        
        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=params)

    def test_executor_execute_not_initialized(self) -> None:
        definition = GenReadmeCommandDefinition()
        executor = GenReadmeCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False
        
        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = GenReadmeCommandDefinition()
        executor = GenReadmeCommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))
