import click

from menu.delete.ocp.cilium.bgp import delete_ocp_cilium_bgp_command
from menu.delete.ocp.cilium.inb import delete_ocp_cilium_inb_command
from menu.delete.ocp.cilium.mesh import delete_ocp_cilium_mesh_command
from menu.delete.ocp.cilium.pnet import delete_ocp_cilium_pnet_command
from menu.delete.ocp.cilium.timescape import delete_ocp_cilium_timescape_command


class Failure(Exception):
    pass


@click.group("cilium")
@click.pass_obj
def delete_ocp_cilium_menu(ctx):
    """OCP Cilium Actions and Settings"""


delete_ocp_cilium_menu.add_command(delete_ocp_cilium_bgp_command)
delete_ocp_cilium_menu.add_command(delete_ocp_cilium_inb_command)
delete_ocp_cilium_menu.add_command(delete_ocp_cilium_mesh_command)
delete_ocp_cilium_menu.add_command(delete_ocp_cilium_pnet_command)
delete_ocp_cilium_menu.add_command(delete_ocp_cilium_timescape_command)
