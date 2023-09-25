import click

from menu.get.aci.xd.server.lldp import get_aci_xd_server_lldp_command


class Failure(Exception):
    pass


@click.group("server")
@click.pass_obj
def get_aci_xd_server_menu(ctx):
    """Get aci cross-domain server commands"""


get_aci_xd_server_menu.add_command(get_aci_xd_server_lldp_command)
