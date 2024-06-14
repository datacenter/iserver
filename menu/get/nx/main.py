import click

from menu.get.nx.config import get_nx_config_command
from menu.get.nx.device import get_nx_device_command
from menu.get.nx.lacp import get_nx_lacp_command
from menu.get.nx.lldp import get_nx_lldp_command
from menu.get.nx.mac import get_nx_mac_command
from menu.get.nx.psirt import get_nx_psirt_command
from menu.get.nx.server import get_nx_server_command
from menu.get.nx.ver import get_nx_ver_command


class Failure(Exception):
    pass


@click.group("nx")
@click.pass_obj
def get_nx_menu(ctx):
    """Get nexus commands"""


get_nx_menu.add_command(get_nx_config_command)
get_nx_menu.add_command(get_nx_device_command)
get_nx_menu.add_command(get_nx_lacp_command)
get_nx_menu.add_command(get_nx_lldp_command)
get_nx_menu.add_command(get_nx_mac_command)
get_nx_menu.add_command(get_nx_psirt_command)
get_nx_menu.add_command(get_nx_server_command)
get_nx_menu.add_command(get_nx_ver_command)
