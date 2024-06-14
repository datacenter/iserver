import click

from menu.set.server.locator.on import set_server_locator_on_command
from menu.set.server.locator.off import set_server_locator_off_command


class Failure(Exception):
    pass


@click.group("locator")
@click.pass_obj
def set_server_locator_menu(ctx):
    """Set server locator commands"""


set_server_locator_menu.add_command(set_server_locator_on_command)
set_server_locator_menu.add_command(set_server_locator_off_command)
