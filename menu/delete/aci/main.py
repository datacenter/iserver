import click

from menu.delete.aci.controller import delete_aci_controller_command


class Failure(Exception):
    pass


@click.group("aci")
@click.pass_obj
def delete_aci_menu(ctx):
    """Delete aci commands"""


delete_aci_menu.add_command(delete_aci_controller_command)
