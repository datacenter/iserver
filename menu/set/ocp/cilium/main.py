import click

from menu.set.ocp.cilium.bgp import set_ocp_cilium_bgp_command
from menu.set.ocp.cilium.config import set_ocp_cilium_config_command
from menu.set.ocp.cilium.image import set_ocp_cilium_image_command
from menu.set.ocp.cilium.inb import set_ocp_cilium_inb_command
from menu.set.ocp.cilium.mesh import set_ocp_cilium_mesh_command
from menu.set.ocp.cilium.plan import set_ocp_cilium_plan_command
from menu.set.ocp.cilium.pnet import set_ocp_cilium_pnet_command
from menu.set.ocp.cilium.restart import set_ocp_cilium_restart_command
from menu.set.ocp.cilium.timescape import set_ocp_cilium_timescape_command


class Failure(Exception):
    pass


@click.group("cilium")
@click.pass_obj
def set_ocp_cilium_menu(ctx):
    """OCP Cilium Actions and Settings"""


set_ocp_cilium_menu.add_command(set_ocp_cilium_bgp_command)
set_ocp_cilium_menu.add_command(set_ocp_cilium_config_command)
set_ocp_cilium_menu.add_command(set_ocp_cilium_image_command)
set_ocp_cilium_menu.add_command(set_ocp_cilium_inb_command)
set_ocp_cilium_menu.add_command(set_ocp_cilium_mesh_command)
set_ocp_cilium_menu.add_command(set_ocp_cilium_plan_command)
set_ocp_cilium_menu.add_command(set_ocp_cilium_pnet_command)
set_ocp_cilium_menu.add_command(set_ocp_cilium_restart_command)
set_ocp_cilium_menu.add_command(set_ocp_cilium_timescape_command)
