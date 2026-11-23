import click

from menu.get.aci.pg.access.intf.main import get_aci_pg_access_interface_menu


class Failure(Exception):
    pass


@click.group("access")
@click.pass_obj
def get_aci_pg_access_menu(ctx):
    """Get aci policy group access commands"""


get_aci_pg_access_menu.add_command(get_aci_pg_access_interface_menu)
