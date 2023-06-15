import click

from menu.set.ocp.node.down import set_ocp_node_down
from menu.set.ocp.node.nestedhv import set_ocp_node_nestedhv
from menu.set.ocp.node.restart import set_ocp_node_restart
from menu.set.ocp.node.up import set_ocp_node_up


class Failure(Exception):
    pass


@click.group("node")
@click.pass_obj
def set_ocp_node_menu(ctx):
    """OCP Node Actions and Settings"""


set_ocp_node_menu.add_command(set_ocp_node_down)
set_ocp_node_menu.add_command(set_ocp_node_nestedhv)
set_ocp_node_menu.add_command(set_ocp_node_restart)
set_ocp_node_menu.add_command(set_ocp_node_up)
