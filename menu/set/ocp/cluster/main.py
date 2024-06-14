import click

from menu.set.ocp.cluster.nestedhv import set_ocp_cluster_nestedhv


class Failure(Exception):
    pass


@click.group("cluster")
@click.pass_obj
def set_ocp_cluster_menu(ctx):
    """OCP Cluster Actions and Settings"""


set_ocp_cluster_menu.add_command(set_ocp_cluster_nestedhv)
