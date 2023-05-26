import click

from menu.get.ocp.cluster.cnv.state import get_ocp_cluster_cnv_state_command


class Failure(Exception):
    pass


@click.group("cnv")
@click.pass_obj
def get_ocp_cluster_cnv_menu(ctx):
    """Get ocp cluster cnv commands"""


get_ocp_cluster_cnv_menu.add_command(get_ocp_cluster_cnv_state_command)
