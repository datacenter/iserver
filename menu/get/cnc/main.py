import click

from menu.get.cnc.controller import get_cnc_controller_command
from menu.get.cnc.node import get_cnc_node_command


class Failure(Exception):
    pass


@click.group("cnc")
@click.pass_obj
def get_cnc_menu(ctx):
    """Get cnc commands"""


get_cnc_menu.add_command(get_cnc_controller_command)
get_cnc_menu.add_command(get_cnc_node_command)
