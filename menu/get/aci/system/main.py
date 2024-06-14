import click

from menu.get.aci.system.fault import get_aci_system_fault_command


class Failure(Exception):
    pass


@click.group("system")
@click.pass_obj
def get_aci_system_menu(ctx):
    """Get aci system commands"""


get_aci_system_menu.add_command(get_aci_system_fault_command)
