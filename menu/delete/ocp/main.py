import click

from menu.delete.ocp.addon.main import delete_ocp_addon_menu
from menu.delete.ocp.cluster import delete_ocp_cluster_command
from menu.delete.ocp.vm import delete_ocp_vm_command


class Failure(Exception):
    pass


@click.group("ocp")
@click.pass_obj
def delete_ocp_menu(ctx):
    """Delete OpenShift commands"""


delete_ocp_menu.add_command(delete_ocp_addon_menu)
delete_ocp_menu.add_command(delete_ocp_cluster_command)
delete_ocp_menu.add_command(delete_ocp_vm_command)
