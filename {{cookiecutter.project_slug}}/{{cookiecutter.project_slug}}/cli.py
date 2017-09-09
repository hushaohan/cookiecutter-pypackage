# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""
import click
from . _module_ import _sub_command_


@click.group()
def entry_point():
    pass


entry_point.add_command(_sub_command_)
