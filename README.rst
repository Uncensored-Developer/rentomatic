==========
rentomatic
==========





Create a simple search engine on top of a dataset of objects which are described by some quantities.


* Free software: MIT license
* Documentation: https://rentomatic.readthedocs.io.


Usage
--------

* Set postgresql connection details in connection_data dictionary in rentomatic/rest/room.py
* install the dependencies in requirements_dev.txt
* run initial_pg_setup.py to setup the postgres database with the table and some data
* to run the project "flask run"
* open 'http://localhost:5000/rooms' to get a list of all the rooms
* filters can be applied like '?filter_code__eq=xxxxxxxxx', '?filter_price__lt=67', '?filter_price__gt=67'.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
