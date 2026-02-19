import click

from menu.set.k8s.node.cordon import set_k8s_node_cordon_command
from menu.set.k8s.node.uncordon import set_k8s_node_uncordon_command


class Failure(Exception):
    pass


@click.group("node")
@click.pass_obj
def set_k8s_node_menu(ctx):
    """K8s node actions and settings"""


set_k8s_node_menu.add_command(set_k8s_node_cordon_command)
set_k8s_node_menu.add_command(set_k8s_node_uncordon_command)
