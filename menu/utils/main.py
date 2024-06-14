import click

from menu.utils.cli.main import utils_cli_menu
from menu.utils.test.main import utils_test_menu
from menu.utils.doc import utils_doc_command


class Failure(Exception):
    pass


@click.group("utils")
@click.pass_obj
def utils_menu(ctx):
    """Developer utilities"""


utils_menu.add_command(utils_cli_menu)
utils_menu.add_command(utils_test_menu)
utils_menu.add_command(utils_doc_command)
