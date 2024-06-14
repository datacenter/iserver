import click

from menu.delete.ocp.addon.main import delete_ocp_addon_menu
from menu.delete.ocp.cluster.main import delete_ocp_cluster_menu


class Failure(Exception):
    pass


@click.group("ocp")
@click.pass_obj
def delete_ocp_menu(ctx):
    """Delete OpenShift commands"""


delete_ocp_menu.add_command(delete_ocp_addon_menu)
delete_ocp_menu.add_command(delete_ocp_cluster_menu)
