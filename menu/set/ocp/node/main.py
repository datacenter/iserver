import click

from menu.set.ocp.node.reboot import set_ocp_node_reboot_command
from menu.set.ocp.node.reload import set_ocp_node_reload_command
from menu.set.ocp.node.shutdown import set_ocp_node_shutdown_command


class Failure(Exception):
    pass


@click.group("node")
@click.pass_obj
def set_ocp_node_menu(ctx):
    """OCP Node Actions and Settings"""


set_ocp_node_menu.add_command(set_ocp_node_reboot_command)
set_ocp_node_menu.add_command(set_ocp_node_reload_command)
set_ocp_node_menu.add_command(set_ocp_node_shutdown_command)
