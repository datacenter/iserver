import click

from menu.set.ocp.cluster.main import set_ocp_cluster_menu
from menu.set.ocp.kubeconfig import set_ocp_kubeconfig
from menu.set.ocp.node.main import set_ocp_node_menu
from menu.set.ocp.vm.main import set_ocp_vm_menu


class Failure(Exception):
    pass


@click.group("ocp")
@click.pass_obj
def set_ocp_menu(ctx):
    """OCP Actions and Settings"""


set_ocp_menu.add_command(set_ocp_cluster_menu)
set_ocp_menu.add_command(set_ocp_kubeconfig)
set_ocp_menu.add_command(set_ocp_node_menu)
set_ocp_menu.add_command(set_ocp_vm_menu)
