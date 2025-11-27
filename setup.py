#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2020 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines setup for tool gen_readme.
'''

from __future__ import print_function
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_readme'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_readme/blob/dev/LICENSE'
__version__: str = '1.1.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

TOOL_DIR = 'gen_readme/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11', '3.12']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS
setup(
    name='gen_readme',
    version='1.1.4',
    description='Readme doc generator',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_readme/',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='Readme, README, project, Unix, Linux, Docs',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_readme', 'gen_readme.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_readme': [
            'py.typed',
            f'{CONF}/gen_readme.logo',
            f'{CONF}/gen_readme.cfg',
            f'{CONF}/gen_readme_util.cfg',
            f'{CONF}/project.yaml',
            f'{TEMPLATE}/README_AVR.template',
            f'{TEMPLATE}/README_C.template',
            f'{TEMPLATE}/README_CC.template',
            f'{TEMPLATE}/README_JS.template',
            f'{TEMPLATE}/README_PL.template',
            f'{TEMPLATE}/README_PY.template',
            f'{TEMPLATE}/README_RPI.template',
            f'{TEMPLATE}/README_SH.template',
            f'{TEMPLATE}/README_STM.template',
            f'{TEMPLATE}/README_VALA.template',
            f'{LOG}/gen_readme.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/gen_readme_run.py'
        ]
    )]
)
