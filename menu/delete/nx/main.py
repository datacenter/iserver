import click

from menu.delete.nx.device import delete_nx_device_command


class Failure(Exception):
    pass


@click.group("nx")
@click.pass_obj
def delete_nx_menu(ctx):
    """Delete nx commands"""


delete_nx_menu.add_command(delete_nx_device_command)
