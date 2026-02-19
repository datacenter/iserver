import click

from menu.delete.imc.cli.main import delete_imc_cli_menu


class Failure(Exception):
    pass


@click.group("imc")
@click.pass_obj
def delete_imc_menu(ctx):
    """Delete imc commands"""


delete_imc_menu.add_command(delete_imc_cli_menu)
