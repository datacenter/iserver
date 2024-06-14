import click

from menu.create.ocp.cluster.bm import create_ocp_cluster_bm_command
from menu.create.ocp.cluster.vsphere import create_ocp_cluster_vshpere_command


class Failure(Exception):
    pass


@click.group("cluster")
@click.pass_obj
def create_ocp_cluster_menu(ctx):
    """Create OpenShift cluster commands"""


create_ocp_cluster_menu.add_command(create_ocp_cluster_bm_command)
create_ocp_cluster_menu.add_command(create_ocp_cluster_vshpere_command)
