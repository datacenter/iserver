import click

from menu.create.aci.mo import create_aci_mo_command


class Failure(Exception):
    pass


@click.group("aci")
@click.pass_obj
def create_aci_menu(ctx):
    """Create aci commands"""


create_aci_menu.add_command(create_aci_mo_command)
