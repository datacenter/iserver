import click

from menu.utils.cli.list import utils_cli_list_command


class Failure(Exception):
    pass


@click.group("cli")
@click.pass_obj
def utils_cli_menu(ctx):
    """Command line"""


utils_cli_menu.add_command(utils_cli_list_command)
