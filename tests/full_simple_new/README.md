<img align="right" src="https://raw.githubusercontent.com/vroncevic/full_simple_new/dev/docs/full_simple_new_logo.png" width="25%">

# full_simple_new

**full_simple_new** TODO.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![full_simple_new python checker](https://github.com/vroncevic/full_simple_new/actions/workflows/full_simple_new_python_checker.yml/badge.svg)](https://github.com/vroncevic/full_simple_new/actions/workflows/full_simple_new_python_checker.yml) [![full_simple_new package checker](https://github.com/vroncevic/full_simple_new/actions/workflows/full_simple_new_package_checker.yml/badge.svg)](https://github.com/vroncevic/full_simple_new/actions/workflows/full_simple_new_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/full_simple_new.svg)](https://github.com/vroncevic/full_simple_new/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/full_simple_new.svg)](https://github.com/vroncevic/full_simple_new/graphs/contributors)

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
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![debian linux os](https://raw.githubusercontent.com/vroncevic/full_simple_new/dev/docs/debtux.png)

[![full_simple_new python3 build](https://github.com/vroncevic/full_simple_new/actions/workflows/full_simple_new_python3_build.yml/badge.svg)](https://github.com/vroncevic/full_simple_new/actions/workflows/full_simple_new_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**full_simple_new** is located at **[pypi.org](https://pypi.org/project/full_simple_new/)**.

You can install by using pip

```bash
# python3
pip3 install full_simple_new
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/full_simple_new/releases/)** download and extract release archive.

To install **full_simple_new** type the following

```bash
tar xvzf full_simple_new-x.y.z.tar.gz
cd full_simple_new-x.y.z/
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/full_simple_new-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/full_simple_new_run.py
ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/full_simple_new_run.py /usr/local/bin/full_simple_new_run.py
```

##### Install using py setup

Navigate to release **[page](https://github.com/vroncevic/full_simple_new/releases/)** download and extract release archive.

To install **full_simple_new** locate and run setup.py with arguments

```bash
tar xvzf full_simple_new-x.y.z.tar.gz
cd full_simple_new-x.y.z/
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use docker to create image/container.

### Dependencies

**full_simple_new** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Library structure

**full_simple_new** is based on OOP

Library structure

```bash

```

### Docs

[![Documentation Status](https://readthedocs.org/projects/full_simple_new/badge/?version=latest)](https://full_simple_new.readthedocs.io/projects/full_simple_new/en/latest/?badge=latest)

More documentation and info at
* [full_simple_new.readthedocs.io](https://full_simple_new.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to full_simple_new](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2023 by [vroncevic.github.io/full_simple_new](https://vroncevic.github.io/full_simple_new/)

**full_simple_new** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/full_simple_new/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)