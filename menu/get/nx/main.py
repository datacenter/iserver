import click

from menu.get.nx.cdp import get_nx_cdp_command
from menu.get.nx.config import get_nx_config_command
from menu.get.nx.device import get_nx_device_command
from menu.get.nx.feature import get_nx_feature_command
from menu.get.nx.hw import get_nx_hardware_command
from menu.get.nx.intf import get_nx_interface_command
from menu.get.nx.lacp import get_nx_lacp_command
from menu.get.nx.lldp import get_nx_lldp_command
from menu.get.nx.mac import get_nx_mac_command
from menu.get.nx.pc import get_nx_pc_command
from menu.get.nx.psirt import get_nx_psirt_command
from menu.get.nx.server import get_nx_server_command
from menu.get.nx.ver import get_nx_ver_command
from menu.get.nx.vlan import get_nx_vlan_command
from menu.get.nx.vpc import get_nx_vpc_command
from menu.get.nx.vrf import get_nx_vrf_command


class Failure(Exception):
    pass


@click.group("nx")
@click.pass_obj
def get_nx_menu(ctx):
    """Get nexus commands"""


get_nx_menu.add_command(get_nx_cdp_command)
get_nx_menu.add_command(get_nx_config_command)
get_nx_menu.add_command(get_nx_device_command)
get_nx_menu.add_command(get_nx_feature_command)
get_nx_menu.add_command(get_nx_hardware_command)
get_nx_menu.add_command(get_nx_interface_command)
get_nx_menu.add_command(get_nx_lacp_command)
get_nx_menu.add_command(get_nx_lldp_command)
get_nx_menu.add_command(get_nx_mac_command)
get_nx_menu.add_command(get_nx_pc_command)
get_nx_menu.add_command(get_nx_psirt_command)
get_nx_menu.add_command(get_nx_server_command)
get_nx_menu.add_command(get_nx_ver_command)
get_nx_menu.add_command(get_nx_vlan_command)
get_nx_menu.add_command(get_nx_vpc_command)
get_nx_menu.add_command(get_nx_vrf_command)
