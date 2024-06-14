import click

from menu.create.ocp.addon.iwo import create_ocp_addon_iwo_command


class Failure(Exception):
    pass


@click.group("addon")
@click.pass_obj
def create_ocp_addon_menu(ctx):
    """Create OpenShift addon commands"""


create_ocp_addon_menu.add_command(create_ocp_addon_iwo_command)
