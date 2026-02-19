import click

from menu.get.imc.cli.main import get_imc_cli_menu


class Failure(Exception):
    pass


@click.group("imc")
@click.pass_obj
def get_imc_menu(ctx):
    """Get imc commands"""


get_imc_menu.add_command(get_imc_cli_menu)
