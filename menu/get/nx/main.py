import click

from menu.get.nx.lldp.main import get_nx_lldp_menu
from menu.get.nx.switch import get_nx_switch_command


class Failure(Exception):
    pass


@click.group("nx")
@click.pass_obj
def get_nx_menu(ctx):
    """Get nexus commands"""


get_nx_menu.add_command(get_nx_lldp_menu)
get_nx_menu.add_command(get_nx_switch_command)
