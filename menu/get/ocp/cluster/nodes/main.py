import click

from menu.get.ocp.cluster.nodes.list import get_ocp_cluster_nodes_list_command
from menu.get.ocp.cluster.nodes.vcenter import get_ocp_cluster_nodes_vcenter_command


class Failure(Exception):
    pass


@click.group("nodes")
@click.pass_obj
def get_ocp_cluster_nodes_menu(ctx):
    """Get ocp cluster nodes commands"""


get_ocp_cluster_nodes_menu.add_command(get_ocp_cluster_nodes_list_command)
get_ocp_cluster_nodes_menu.add_command(get_ocp_cluster_nodes_vcenter_command)
