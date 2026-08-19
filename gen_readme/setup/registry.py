# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core gen_readme components for simplification of gen_readme bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_readme.core.service.iservice import IService
from gen_readme.core.service.isubprocessor import ISubProcessor
from gen_readme.infrastructure.cli.icli import ICLI
from gen_readme.setup.bundle import GenReadmeBundle
from gen_readme.setup.validator import GenReadmeBundleValidator
from gen_readme.setup.keys import GenReadmeBundleKeys
from gen_readme.setup.dependencies import GenReadmeBundleDependencies
from gen_readme.setup.dep_validator import GenReadmeBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_readme'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_readme/blob/dev/LICENSE'
__version__ = '1.1.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenReadmeBundleRegistry:
    '''
        Encapsulates core gen_readme components for simplification of gen_readme bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_readme bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenReadmeBundleDependencies) -> GenReadmeBundle:
        '''
            Creates the gen_readme bundle.

            :param dependencies: The gen_readme bundle dependencies.
            :return: The gen_readme bundle.
            :exceptions:
                | ATSValueError: The gen_readme bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_readme bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_readme bundle must be provided and have proper values.
                | ATSTypeError:  The gen_readme bundle must be an instance of GenReadmeBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenReadmeBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenReadmeBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenReadmeBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenReadmeBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenReadmeBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenReadmeBundle = GenReadmeBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenReadmeBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
