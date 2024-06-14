import click

from menu.get.aci.pg.access.main import get_aci_pg_access_menu


class Failure(Exception):
    pass


@click.group("pg")
@click.pass_obj
def get_aci_pg_menu(ctx):
    """Get aci policy group commands"""


get_aci_pg_menu.add_command(get_aci_pg_access_menu)
