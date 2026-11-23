import click

from menu.set.nx.device import set_nx_device_command
from menu.set.nx.ws import set_nx_ws_command


class Failure(Exception):
    pass


@click.group("nx")
@click.pass_obj
def set_nx_menu(ctx):
    """Set nexus commands"""


set_nx_menu.add_command(set_nx_device_command)
set_nx_menu.add_command(set_nx_ws_command)
