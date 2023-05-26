import click

from menu.get.nexus.lldp.neighbors import get_nexus_lldp_neighbors_command


class Failure(Exception):
    pass


@click.group("lldp")
@click.pass_obj
def get_nexus_lldp_menu(ctx):
    """Get nexus lldp commands"""


get_nexus_lldp_menu.add_command(get_nexus_lldp_neighbors_command)
