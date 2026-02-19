import click

from menu.set.imc.cli.boot_order import set_imc_cli_boot_order_command
from menu.set.imc.cli.endpoint import set_imc_cli_endpoint_command


class Failure(Exception):
    pass


@click.group("cli")
@click.pass_obj
def set_imc_cli_menu(ctx):
    """IMC cli actions and settings"""


set_imc_cli_menu.add_command(set_imc_cli_boot_order_command)
set_imc_cli_menu.add_command(set_imc_cli_endpoint_command)
