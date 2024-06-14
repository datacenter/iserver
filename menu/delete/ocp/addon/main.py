import click

from menu.delete.ocp.addon.iwo import delete_ocp_addon_iwo_command


class Failure(Exception):
    pass


@click.group("addon")
@click.pass_obj
def delete_ocp_addon_menu(ctx):
    """Delete OpenShift addon commands"""


delete_ocp_addon_menu.add_command(delete_ocp_addon_iwo_command)
