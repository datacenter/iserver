import click

from menu.create.ocp.addon.main import create_ocp_addon_menu
from menu.create.ocp.cluster.main import create_ocp_cluster_menu
from menu.create.ocp.migrate import create_ocp_migrate_command


class Failure(Exception):
    pass


@click.group("ocp")
@click.pass_obj
def create_ocp_menu(ctx):
    """Create OpenShift commands"""


create_ocp_menu.add_command(create_ocp_addon_menu)
create_ocp_menu.add_command(create_ocp_cluster_menu)
create_ocp_menu.add_command(create_ocp_migrate_command)
