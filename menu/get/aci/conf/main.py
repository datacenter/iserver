import click

from menu.get.aci.conf.intf import get_aci_configuration_interface_command
from menu.get.aci.conf.switch import get_aci_configuration_switch_command


class Failure(Exception):
    pass


@click.group("conf")
@click.pass_obj
def get_aci_conf_menu(ctx):
    """Get aci configuration commands"""


get_aci_conf_menu.add_command(get_aci_configuration_interface_command)
get_aci_conf_menu.add_command(get_aci_configuration_switch_command)
