# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
{% if cookiecutter.project_type == 'Personal' %}
__email__ = '{{ cookiecutter.personal_email }}'
{% elif cookiecutter.project_type == 'Work' %}
__email__ = '{{ cookiecutter.work_email }}'
{% endif %}
__version__ = '{{ cookiecutter.version }}'
