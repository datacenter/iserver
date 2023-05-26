import click

from menu.set.aci.controller import set_aci_controller_command


class Failure(Exception):
    pass


@click.group("aci")
@click.pass_obj
def set_aci_menu(ctx):
    """Set aci commands"""


set_aci_menu.add_command(set_aci_controller_command)
