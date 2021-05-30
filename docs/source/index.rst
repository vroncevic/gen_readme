Create README.md doc module
----------------------------

**gen_readme** is tool for creating README.md doc module.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/gen_readme/workflows/Python%20package%20gen_readme/badge.svg
   :target: https://github.com/vroncevic/gen_readme/workflows/Python%20package%20gen_readme/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/gen_readme.svg
   :target: https://github.com/vroncevic/gen_readme/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_readme.svg
   :target: https://github.com/vroncevic/gen_readme/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/gen_readme/badge/?version=latest
   :target: https://gen_readme.readthedocs.io/projects/gen_readme/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/gen_readme/workflows/Install%20Python2%20Package%20gen_readme/badge.svg
   :target: https://github.com/vroncevic/gen_readme/workflows/Install%20Python2%20Package%20gen_readme/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/gen_readme/workflows/Install%20Python3%20Package%20gen_readme/badge.svg
   :target: https://github.com/vroncevic/gen_readme/workflows/Install%20Python3%20Package%20gen_readme/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_readme/releases

To install this set of modules type the following:

.. code-block:: bash

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

You can use Docker to create image/container, or You can use pip to install:

.. code-block:: bash

    #python2
    pip install gen_readme
    #python3
    pip3 install gen_readme

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/gen_readme/workflows/gen_readme%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/gen_readme/actions?query=workflow%3A%22gen_readme+docker+checker%22

Dependencies
-------------

**gen_readme** requires next modules and libraries:

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_readme** is based on OOP:

Code structure:

.. code-block:: bash

    gen_readme/
    ├── conf/
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

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2020 by `vroncevic.github.io/gen_readme <https://vroncevic.github.io/gen_readme>`_

**gen_readme** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_readme/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
