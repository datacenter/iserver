import click

from menu.get.nexus.lldp.main import get_nexus_lldp_menu
from menu.get.nexus.switch import get_nexus_switch_command


class Failure(Exception):
    pass


@click.group("nexus")
@click.pass_obj
def get_nexus_menu(ctx):
    """Get nexus commands"""


get_nexus_menu.add_command(get_nexus_lldp_menu)
get_nexus_menu.add_command(get_nexus_switch_command)
