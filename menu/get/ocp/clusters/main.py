import click

from menu.get.ocp.clusters.console import get_ocp_clusters_console_command
from menu.get.ocp.clusters.iwo import get_ocp_clusters_iwo_command
from menu.get.ocp.clusters.kc import get_ocp_clusters_kc_command
from menu.get.ocp.clusters.list import get_ocp_clusters_list_command
from menu.get.ocp.clusters.rh import get_ocp_clusters_rh_command
from menu.get.ocp.clusters.virt import get_ocp_clusters_virt_command


class Failure(Exception):
    pass


@click.group("clusters")
@click.pass_obj
def get_ocp_clusters_menu(ctx):
    """Get ocp clusters commands"""


get_ocp_clusters_menu.add_command(get_ocp_clusters_console_command)
get_ocp_clusters_menu.add_command(get_ocp_clusters_iwo_command)
get_ocp_clusters_menu.add_command(get_ocp_clusters_kc_command)
get_ocp_clusters_menu.add_command(get_ocp_clusters_list_command)
get_ocp_clusters_menu.add_command(get_ocp_clusters_rh_command)
get_ocp_clusters_menu.add_command(get_ocp_clusters_virt_command)
