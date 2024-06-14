import click

from menu.set.aci.cache import set_aci_cache_command
from menu.set.aci.controller import set_aci_controller_command
from menu.set.aci.mode import set_aci_mode_command
from menu.set.aci.ws import set_aci_ws_command


class Failure(Exception):
    pass


@click.group("aci")
@click.pass_obj
def set_aci_menu(ctx):
    """Set aci commands"""


set_aci_menu.add_command(set_aci_cache_command)
set_aci_menu.add_command(set_aci_controller_command)
set_aci_menu.add_command(set_aci_mode_command)
set_aci_menu.add_command(set_aci_ws_command)
