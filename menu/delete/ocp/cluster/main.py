import click

from menu.delete.ocp.cluster.vsphere import delete_ocp_cluster_vshpere_command


class Failure(Exception):
    pass


@click.group("cluster")
@click.pass_obj
def delete_ocp_cluster_menu(ctx):
    """Delete OpenShift cluster commands"""


delete_ocp_cluster_menu.add_command(delete_ocp_cluster_vshpere_command)
