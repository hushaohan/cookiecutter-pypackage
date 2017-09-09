Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================

Contents:

.. toctree::
   :maxdepth: 2

   readme
   installation
   usage
   modules
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
