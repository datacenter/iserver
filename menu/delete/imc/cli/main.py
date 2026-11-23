import click

from menu.delete.imc.cli.boot_device import delete_imc_cli_boot_device_command


class Failure(Exception):
    pass


@click.group("cli")
@click.pass_obj
def delete_imc_cli_menu(ctx):
    """Delete imc cli commands"""


delete_imc_cli_menu.add_command(delete_imc_cli_boot_device_command)
