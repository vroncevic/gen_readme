# -*- coding: UTF-8 -*-

'''
Module
    engine.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_readme is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_readme is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Main engine orchestrator class for Task Code Generator CLI.
'''

from typing import Any, override
from os.path import dirname, realpath
from ats_utilities.base.engine import Base
from ats_utilities.base.component_bundle import BaseComponentBundle
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.exceptions.ats_value_error import ATSValueError
from gen_readme.gen_readme_bundle import GenReadmeBundle
from gen_readme.domain.ports.itemplate_provider import ITemplateProvider
from gen_readme.infrastructure.template_provider import TemplateProvider
from gen_readme.domain.ports.ifile_writer import IFileWriter
from gen_readme.infrastructure.file_writer import FileWriter
from gen_readme.domain.ports.ifile_gen import IFileGen
from gen_readme.application.service import FileGen
from gen_readme.application.service_bundle import ServiceBundle
from gen_readme.infrastructure.icli_command import ICLICommand
from gen_readme.infrastructure.cli_bundle import CLIBundle
from gen_readme.infrastructure.gen_readme_command import GenReadmeCommand
from gen_readme.infrastructure.icli import ICLI
from gen_readme.infrastructure.cli import CLI

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_readme'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_readme/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class GenReadme(Base):
    '''
        Engine orchestrating the initialization and execution of GenReadme.

        It defines:

            :attributes:
                | _info_file - Path to the info file.
                | _cli - Adapter for command line user interface.
            :methods:
                | __init__ - Initializes the GenReadme engine with adapters and services.
                | process - Processes the gen_readme.
    '''

    _info_file: str = 'infrastructure/config/gen_readme.cfg'

    def __init__(self, component_bundle: GenReadmeBundle | None = None) -> None:
        '''
            Initializes the GenReadme engine with adapters and services.

            :param component_bundle: GenReadme bundle containing adapters and services | None.
            :type component_bundle: <GenReadmeBundle | None>
            :exceptions: None.
        '''
        current_dir: str = dirname(realpath(__file__))
        super().__init__(BaseComponentBundle(info_file=f'{current_dir}/{self._info_file}'))

        try:
            if not self._is_initialized:
                raise ATSValueError(f'failed to initialize engine with {current_dir}/{self._info_file}')

            # Mark as not initialized (waiting for other components to be initialized)
            self._is_initialized = False

            # Use provided component bundle or use default adapters
            bundle: GenReadmeBundle = component_bundle or GenReadmeBundle()

            # Initialization of secondary adapters (Infrastructure)
            template_provider: ITemplateProvider = bundle.template_provider or TemplateProvider()
            file_writer: IFileWriter = bundle.file_writer or FileWriter()

            # Initialization of option manager adapter (Adapter for options parsing)
            parser: IOptionManager = bundle.parser or self._options_parser

            # Injecting adapters into the application service (Orchestration)
            service_bundle: ServiceBundle = ServiceBundle(
                template_provider=template_provider, file_writer=file_writer
            )
            service: IFileGen = bundle.service or FileGen(service_bundle)

            # Setting up CLI command strategies (Command strategies for CLI)
            commands: list[ICLICommand] = [GenReadmeCommand()]

            # Setting up primary adapter (CLI interface)
            cli_bundle: CLIBundle = CLIBundle(service=service, parser=parser, commands=commands)
            self._cli: ICLI = bundle.cli or CLI(cli_bundle)

            # Mark as initialized (all components initialized)
            self._is_initialized = all([
               component.is_initialized() for component in [template_provider, file_writer, service, self._cli] if component
            ])
            self._reporter.success(["✅ gen_readme: engine initialized successfully."])

        except (ATSValueError, ValueError) as exc:
            self._reporter.error([f'❌ gen_readme: {exc}'])
        except Exception as exc:
            self._reporter.error([f'❌ gen_readme unexpected exception: {exc}'])

    @override
    def process(self) -> None:
        '''
            Process the CLI adapter to run the tool command.

            :exceptions: None.
        '''
        result: dict[str, Any] = {}

        try:
            if self.is_initialized():
                self._reporter.success(["🔥 Starting execution command..."])
                result = self._cli.run()
                self._reporter.success(["✅ Execution finished!"])

                if result.get("returncode") != 0:
                    self._reporter.error([f'❌ gen_readme: {result.get("stderr")}'])
                    self._reporter.error([f'❌ gen_readme: exiting with error.'])
                else:
                    self._reporter.success([f'✅ gen_readme: {result.get("stdout") or 'done!'}'])
                    self._reporter.success([f'✅ gen_readme: exiting successfully.'])
            else:
                self._reporter.error([f'❌ gen_readme: engine not initialized.'])

        except (ATSValueError, ValueError) as exc:
            self._reporter.error([f'❌ gen_readme: {exc}'])
        except Exception as exc:
            self._reporter.error([f'❌ gen_readme unexpected exception: {exc}'])
