import click

from menu.get.ucsm.inventory import get_ucsm_inventory_command
from menu.get.ucsm.chassis import get_ucsm_chassis_command
from menu.get.ucsm.chassiz import get_ucsm_chassiz_command
from menu.get.ucsm.blades import get_ucsm_blades_command
from menu.get.ucsm.blade import get_ucsm_blade_command
from menu.get.ucsm.manager import get_ucsm_manager_command
from menu.get.ucsm.query import get_ucsm_query_command


class Failure(Exception):
    pass


@click.group("ucsm")
@click.pass_obj
def get_ucsm_menu(ctx):
    """Get ucsm commands"""


get_ucsm_menu.add_command(get_ucsm_inventory_command)
get_ucsm_menu.add_command(get_ucsm_chassis_command)
get_ucsm_menu.add_command(get_ucsm_chassiz_command)
get_ucsm_menu.add_command(get_ucsm_blades_command)
get_ucsm_menu.add_command(get_ucsm_blade_command)
get_ucsm_menu.add_command(get_ucsm_manager_command)
get_ucsm_menu.add_command(get_ucsm_query_command)
