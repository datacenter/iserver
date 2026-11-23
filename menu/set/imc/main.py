import click

from menu.set.imc.cli.main import set_imc_cli_menu


class Failure(Exception):
    pass


@click.group("imc")
@click.pass_obj
def set_imc_menu(ctx):
    """IMC actions and settings"""


set_imc_menu.add_command(set_imc_cli_menu)
