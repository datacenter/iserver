import click

from menu.create.imc.cli.boot_device import create_imc_cli_boot_device_command


class Failure(Exception):
    pass


@click.group("cli")
@click.pass_obj
def create_imc_cli_menu(ctx):
    """Create imc cli commands"""


create_imc_cli_menu.add_command(create_imc_cli_boot_device_command)
