import click

from menu.create.imc.cli.main import create_imc_cli_menu


class Failure(Exception):
    pass


@click.group("imc")
@click.pass_obj
def create_imc_menu(ctx):
    """Create imc commands"""


create_imc_menu.add_command(create_imc_cli_menu)
