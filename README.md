<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_readme/dev/docs/gen_readme_logo.png" width="25%">

# Create README.md doc module

**gen_readme** is tool for creating README.md doc module.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_readme/workflows/Python%20package%20gen_readme/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_readme.svg)](https://github.com/vroncevic/gen_readme/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_readme.svg)](https://github.com/vroncevic/gen_readme/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**

- [Installation](#installation)
  - [Install using pip](#install-using-pip)
  - [Install using setuptools](#install-using-setuptools)
  - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/gen_readme/workflows/Install%20Python2%20Package%20gen_readme/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_readme/workflows/Install%20Python3%20Package%20gen_readme/badge.svg?branch=master)

Currently there are three ways to install tool

- Install process based on pip
- Install process based on setup.py (setuptools)
- Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen_readme/)**.

You can install by using pip

```bash
#python2
pip install gen_readme
#python3
pip3 install gen_readme
```

##### Install using setuptools

Navigate to **[release page](https://github.com/vroncevic/gen_readme/releases)** download and extract release archive.

To install modules, locate and run setup.py, type the following

```bash
tar xvzf gen_readme-x.y.z.tar.gz
cd gen_readme-x.y.z
#python2
pip install -r requirements.txt
python setup.py install_lib
python setup.py install_egg_info
python setup.py install_data
#python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
python3 setup.py install_data
```

##### Install using docker

You can use Dockerfile to create image/container.

[![gen_readme docker checker](https://github.com/vroncevic/gen_readme/workflows/gen_readme%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_readme/actions?query=workflow%3A%22gen_readme+docker+checker%22)

### Dependencies

**gen_readme** requires next modules and libraries

- [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Tool structure

**gen_readme** is based on OOP

Generator structure

```bash
gen_readme/
├── conf/
│   ├── gen_readme.logo
│   ├── gen_readme.cfg
│   ├── gen_readme_util.cfg
│   ├── project.yaml
│   └── template/
│       ├── README_AVR.template
│       ├── README_CC.template
│       ├── README_C.template
│       ├── README_JS.template
│       ├── README_PL.template
│       ├── README_PY.template
│       ├── README_RPI.template
│       ├── README_SH.template
│       ├── README_STM.template
│       └── README_VALA.template
├── __init__.py
├── log/
│   └── gen_readme.log
├── pro/
│   ├── __init__.py
│   ├── read_template.py
│   └── write_template.py
└── run/
    └── gen_readme_run.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_readme/badge/?version=latest)](https://gen_readme.readthedocs.io/projects/gen_readme/en/latest/?badge=latest)

More documentation and info at

- [gen_readme.readthedocs.io](https://gen_readme.readthedocs.io/en/latest/)
- [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2020 by [vroncevic.github.io/gen_readme](https://vroncevic.github.io/gen_readme/)

**gen_readme** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_readme/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
