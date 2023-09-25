import click

from menu.create.ocp.addon.main import create_ocp_addon_menu
from menu.create.ocp.cluster import create_ocp_cluster_command
from menu.create.ocp.ssh import create_ocp_ssh_command
from menu.create.ocp.vm import create_ocp_vm_command


class Failure(Exception):
    pass


@click.group("ocp")
@click.pass_obj
def create_ocp_menu(ctx):
    """Create OpenShift commands"""


create_ocp_menu.add_command(create_ocp_addon_menu)
create_ocp_menu.add_command(create_ocp_cluster_command)
create_ocp_menu.add_command(create_ocp_ssh_command)
create_ocp_menu.add_command(create_ocp_vm_command)
