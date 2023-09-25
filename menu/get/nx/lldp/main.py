import click

from menu.get.nx.lldp.neighbors import get_nx_lldp_neighbors_command


class Failure(Exception):
    pass


@click.group("lldp")
@click.pass_obj
def get_nx_lldp_menu(ctx):
    """Get nx lldp commands"""


get_nx_lldp_menu.add_command(get_nx_lldp_neighbors_command)
