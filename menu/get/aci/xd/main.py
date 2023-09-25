import click

from menu.get.aci.xd.server.main import get_aci_xd_server_menu


class Failure(Exception):
    pass


@click.group("xd")
@click.pass_obj
def get_aci_xd_menu(ctx):
    """Get aci cross domain commands"""


get_aci_xd_menu.add_command(get_aci_xd_server_menu)
