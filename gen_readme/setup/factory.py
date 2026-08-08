# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_readme bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_readme.setup.bundle import GenReadmeBundle
from gen_readme.setup.options import GenReadmeBundleOptions
from gen_readme.setup.registry import GenReadmeBundleRegistry
from gen_readme.setup.dependencies import GenReadmeBundleDependencies
from gen_readme.setup.opt_validator import GenReadmeBundleOptionsValidator
from gen_readme.setup.keys import GenReadmeBundleKeys
from gen_readme.core.service.engine import Service
from gen_readme.infrastructure.subprocessor import SubProcessor
from gen_readme.infrastructure.cli.engine import CLI
from gen_readme.infrastructure.cli.setup.bundle import CLIBundle
from gen_readme.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_readme.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_readme.infrastructure.command.command import CommandBundle
from gen_readme.infrastructure.command.gen_readme_command_definition import GenReadmeCommandDefinition
from gen_readme.infrastructure.command.gen_readme_command_executor import GenReadmeCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_readme'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_readme/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenReadmeBundleFactory:
    '''
        Factory for creating the gen_readme bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_readme info file.
            :methods:
                | create_bundle - Creates the gen_readme bundle with optional pre-configured options.
    '''

    _info_file: str = 'gen_readme/infrastructure/config/gen_readme.cfg'

    @classmethod
    def create_bundle(cls, options: GenReadmeBundleOptions | None = None) -> GenReadmeBundle:
        '''
            Creates the gen_readme bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_readme bundle.
            :return: The gen_readme bundle.
            :exceptions:
                | ATSValueError: The gen_readme bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_readme bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_readme bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_readme bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_readme bundle must be provided and have proper values.
                | ATSTypeError:  The gen_readme bundle must be an instance of GenReadmeBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenReadmeBundleOptionsValidator.validate(options)

        info_file = options.get(GenReadmeBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_readme_definition: GenReadmeCommandDefinition = GenReadmeCommandDefinition()

        gen_readme_bundle: CommandBundle = CommandBundle(
            definition=gen_readme_definition,
            executor=GenReadmeCommandExecutor(gen_readme_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_readme_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenReadmeBundleRegistry.create_bundle(
            dependencies=GenReadmeBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )
