import click

from menu.get.aci.pg.access.intf.port import get_aci_pg_access_interface_port_command
from menu.get.aci.pg.access.intf.vpc import get_aci_pg_access_interface_vpc_command


class Failure(Exception):
    pass


@click.group("intf")
@click.pass_obj
def get_aci_pg_access_interface_menu(ctx):
    """Get aci policy group access interface commands"""


get_aci_pg_access_interface_menu.add_command(get_aci_pg_access_interface_port_command)
get_aci_pg_access_interface_menu.add_command(get_aci_pg_access_interface_vpc_command)
