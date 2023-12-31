Create README.md doc module
----------------------------

**gen_readme** is tool for creating README.md doc module.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_readme python checker| |gen_readme python package| |github issues| |documentation status| |github contributors|

.. |gen_readme python checker| image:: https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_python_checker.yml

.. |gen_readme python package| image:: https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_readme.svg
   :target: https://github.com/vroncevic/gen_readme/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_readme.svg
   :target: https://github.com/vroncevic/gen_readme/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_readme/badge/?version=latest
   :target: https://gen-readme.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_readme python3 build|

.. |gen_readme python3 build| image:: https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_readme/actions/workflows/gen_readme_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_readme/releases

To install this set of modules type the following

.. code-block:: bash

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

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen_readme

Dependencies
-------------

**gen_readme** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_readme** is based on OOP

Code structure

.. code-block:: bash

    gen_readme/
        ├── conf/
        │   ├── gen_readme.cfg
        │   ├── gen_readme.logo
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
        
        6 directories, 20 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2020 - 2024 by `vroncevic.github.io/gen_readme <https://vroncevic.github.io/gen_readme>`_

**gen_readme** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_readme/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
