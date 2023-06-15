import click

from menu.set.ucsm.manager import set_ucsm_manager_command
from menu.set.ucsm.inventory import set_ucsm_inventory_command


class Failure(Exception):
    pass


@click.group("ucsm")
@click.pass_obj
def set_ucsm_menu(ctx):
    """Set ucsm commands"""


set_ucsm_menu.add_command(set_ucsm_manager_command)
set_ucsm_menu.add_command(set_ucsm_inventory_command)
