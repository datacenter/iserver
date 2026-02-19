import click

from menu.get.ocp.cilium.agent import get_ocp_cilium_agent_command
from menu.get.ocp.cilium.bgp import get_ocp_cilium_bgp_command
from menu.get.ocp.cilium.config import get_ocp_cilium_config_command
from menu.get.ocp.cilium.inb import get_ocp_cilium_inb_command
from menu.get.ocp.cilium.mesh import get_ocp_cilium_mesh_command
from menu.get.ocp.cilium.operator import get_ocp_cilium_operator_command
from menu.get.ocp.cilium.package import get_ocp_cilium_package_command
from menu.get.ocp.cilium.pnet import get_ocp_cilium_pnet_command
from menu.get.ocp.cilium.pod import get_ocp_cilium_pod_command
from menu.get.ocp.cilium.state import get_ocp_cilium_state_command
from menu.get.ocp.cilium.timescape import get_ocp_cilium_timescape_command


class Failure(Exception):
    pass


@click.group("cilium")
@click.pass_obj
def get_ocp_cilium_menu(ctx):
    """Get ocp cilium commands"""


get_ocp_cilium_menu.add_command(get_ocp_cilium_agent_command)
get_ocp_cilium_menu.add_command(get_ocp_cilium_bgp_command)
get_ocp_cilium_menu.add_command(get_ocp_cilium_config_command)
get_ocp_cilium_menu.add_command(get_ocp_cilium_inb_command)
get_ocp_cilium_menu.add_command(get_ocp_cilium_mesh_command)
get_ocp_cilium_menu.add_command(get_ocp_cilium_operator_command)
get_ocp_cilium_menu.add_command(get_ocp_cilium_package_command)
get_ocp_cilium_menu.add_command(get_ocp_cilium_pnet_command)
get_ocp_cilium_menu.add_command(get_ocp_cilium_pod_command)
get_ocp_cilium_menu.add_command(get_ocp_cilium_state_command)
get_ocp_cilium_menu.add_command(get_ocp_cilium_timescape_command)
