# -*- coding: UTF-8 -*-

'''
Module
    gen_config_command.py
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
    Defines GenReadmeCommand class implementing ICLICommand strategy.
'''

from datetime import date
from typing import Any, override
from ats_utilities.option.command_option import CommandOption
from ats_utilities.factory_class import format_instance_to_string
from gen_readme.infrastructure.icli_command import ICLICommand
from gen_readme.domain.ports.ifile_gen import IFileGen

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_readme'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_readme/blob/dev/LICENSE'
__version__: str = '1.1.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class GenReadmeCommand(ICLICommand):
    '''
        CLI subcommand for generating Readme.

        It defines:

            :attributes: None.
            :methods:
                | name - Returns the command name key.
                | help_text - Returns the command help text.
                | options - Returns the command options.
                | execute - Executes the configuration file generation logic.
                | __str__ - Returns GenReadmeCommand instance as string representation.
    '''

    @property
    @override
    def name(self) -> str:
        '''
            Returns the command name key.

            :return: The command name key.
            :rtype: <str>
            :exceptions: None.
        '''
        return "generate-readme"

    @property
    @override
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
            :rtype: <str>
            :exceptions: None.
        '''
        return "Generate README.md file"

    @property
    @override
    def options(self) -> list[CommandOption]:
        '''
            Returns the command options.

            :return: List of command options.
            :rtype: <List[CommandOption]>
            :exceptions: None.
        '''
        return [
            CommandOption(
                name="--type",
                help_text="Type of the project",
                required=True,
                choices=["avr", "c", "cc", "js", "pl", "py", "rpi", "sh", "stm", "vala"],
                default="py"
            ),
            CommandOption(
                name="--project-name",
                help_text="Project name",
                required=True
            ),
            CommandOption(
                name="--version",
                help_text="Project version",
                required=True
            ),
            CommandOption(
                name="--description",
                help_text="Project description",
                required=True
            ),
            CommandOption(
                name="--author-name",
                help_text="Author name",
                required=True
            ),
            CommandOption(
                name="--author-url",
                help_text="Author URL",
                required=True
            ),
            CommandOption(
                name="--license",
                help_text="Project license",
                required=True
            ),
            CommandOption(
                name="--repo-url",
                help_text="Repository URL",
                required=True
            ),
            CommandOption(
                name="--filename",
                help_text="Target filename",
                required=False,
                default="README.md"
            )
        ]

    @override
    def execute(self, params: dict[str, Any], service: IFileGen) -> dict[str, Any]:
        '''
            Executes the configuration file generation logic.

            :param params: Subcommand parameters from CLI parser.
            :type params: <dict[str, Any]>
            :param service: Generation orchestrator service instance.
            :type service: <IFileGen>
            :return: Return code, stdout and stderr messages.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        target_filename = params.pop("filename", "README.md")
        project_type = params.get("type", "py").upper()
        template_name = f"README_{project_type}"
        params["PRO"] = params.get("project_name")
        params["YEAR"] = str(date.today().year)
        params["VERSION"] = params.get("version")
        params["DESCRIPTION"] = params.get("description")
        params["AUTHOR_NAME"] = params.get("author_name")
        params["AUTHOR_URL"] = params.get("author_url")
        params["LICENSE"] = params.get("license")
        params["REPO_URL"] = params.get("repo_url")

        return service.execute(
            template_name=template_name,
            target_filename=target_filename,
            cli_params=params
        )

    @override
    def __str__(self) -> str:
        '''
            Returns GenReadmeCommand instance as string representation.

            :return: GenReadmeCommand instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
