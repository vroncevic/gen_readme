<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_readme/dev/docs/gen_readme_logo.png" width="25%">

# Create README.md doc module

**gen_readme** is tool for creating README.md doc module.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_readme python checker](https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_python_checker.yml) [![gen_readme package checker](https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_readme.svg)](https://github.com/vroncevic/gen_readme/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_readme.svg)](https://github.com/vroncevic/gen_readme/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Code coverage](#code-coverage)
- [Usage](#usage)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_readme/dev/docs/debtux.png)

[![gen_readme python3 build](https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen_readme/)**.

You can install by using pip

```bash
#python3
pip3 install gen_readme
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_readme/releases/)** download and extract release archive.

To install **gen_readme** type the following

```bash
tar xvzf gen_readme-x.y.z.tar.gz
cd gen_readme-x.y.z/
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_readme-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_readme_run.py
ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_readme_run.py /usr/local/bin/gen_readme_run.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_readme/releases)** download and extract release archive.

To install **gen_readme** locate and run setup.py, type the following

```bash
tar xvzf gen_readme-x.y.z.tar.gz
cd gen_readme-x.y.z
#python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
python3 setup.py install_data
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**gen_readme** requires next modules and libraries

- [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Tool structure

**gen_readme** is based on OOP

Generator structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    gen_readme/
         ├── application/
         │   ├── __init__.py
         │   ├── service.py
         │   └── service_bundle.py
         ├── domain/
         │   ├── __init__.py
         │   ├── models.py
         │   └── ports/
         │       ├── ifile_gen.py
         │       ├── ifile_writer.py
         │       ├── __init__.py
         │       └── itemplate_provider.py
         ├── engine.py
         ├── gen_readme_bundle.py
         ├── infrastructure/
         │   ├── cli.py
         │   ├── cli_bundle.py
         │   ├── config/
         │   │   ├── gen_readme.cfg
         │   │   └── gen_readme.logo
         │   ├── file_writer.py
         │   ├── gen_readme_command.py
         │   ├── icli.py
         │   ├── icli_command.py
         │   ├── __init__.py
         │   ├── template_provider.py
         │   └── templates/
         │       ├── README_AVR.template
         │       ├── README_C.template
         │       ├── README_CC.template
         │       ├── README_JS.template
         │       ├── README_PL.template
         │       ├── README_PY.template
         │       ├── README_RPI.template
         │       ├── README_SH.template
         │       ├── README_STM.template
         │       └── README_VALA.template
         ├── __init__.py
         └── py.typed

     7 directories, 33 files
```
</details>

### Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_readme/__init__.py` | 8 | 0 | 100%|
| `gen_readme/application/__init__.py` | 8 | 0 | 100%|
| `gen_readme/application/service.py` | 35 | 0 | 100%|
| `gen_readme/application/service_bundle.py` | 29 | 0 | 100%|
| `gen_readme/domain/__init__.py` | 8 | 0 | 100%|
| `gen_readme/domain/models.py` | 20 | 0 | 100%|
| `gen_readme/domain/ports/__init__.py` | 8 | 0 | 100%|
| `gen_readme/domain/ports/ifile_gen.py` | 11 | 0 | 100%|
| `gen_readme/domain/ports/ifile_writer.py` | 10 | 0 | 100%|
| `gen_readme/domain/ports/itemplate_provider.py` | 10 | 0 | 100%|
| `gen_readme/engine.py` | 64 | 0 | 100%|
| `gen_readme/gen_readme_bundle.py` | 41 | 0 | 100%|
| `gen_readme/infrastructure/__init__.py` | 8 | 0 | 100%|
| `gen_readme/infrastructure/cli.py` | 36 | 0 | 100%|
| `gen_readme/infrastructure/cli_bundle.py` | 33 | 0 | 100%|
| `gen_readme/infrastructure/file_writer.py` | 30 | 0 | 100%|
| `gen_readme/infrastructure/gen_readme_command.py` | 44 | 0 | 100%|
| `gen_readme/infrastructure/icli.py` | 11 | 0 | 100%|
| `gen_readme/infrastructure/icli_command.py` | 14 | 0 | 100%|
| `gen_readme/infrastructure/template_provider.py` | 29 | 0 | 100%|
| **Total** | 457 | 0 | 100% |

</details>

### Usage

Install package

```bash
pip3 install gen_readme
```

Prepare main entry point by downloading [main.py](https://raw.githubusercontent.com/vroncevic/gen_readme/master/main.py) or create your own.


```bash
wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_readme/master/main.py
```

Running tool for creating new distributing py module

```bash
python3 main.py generate-readme \
    --type "avr" \
    --project-name "gen_readme" \
    --version "1.1.5" \
    --description "Generate README.md file" \
    --author-name "Vladimir Roncevic" \
    --author-url "https://vroncevic.github.io" \
    --license "MIT" \
    --repo-url "https://github.com/vroncevic/gen_readme" \
    --filename "README_AVR.md"
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_readme/badge/?version=latest)](https://gen-readme.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_readme.readthedocs.io](https://gen-readme.readthedocs.io)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to gen_readme](CONTRIBUTING.md)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2020 - 2026 by [vroncevic.github.io/gen_readme](https://vroncevic.github.io/gen_readme/)

**gen_readme** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_readme/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
