import click

from menu.set.server.locator.main import set_server_locator_menu
from menu.set.server.os_image import set_server_os_image_command
from menu.set.server.power.main import set_server_power_menu
from menu.set.server.scu import set_server_scu_command
from menu.set.server.tag import set_server_tag_command


class Failure(Exception):
    pass


@click.group("server")
@click.pass_obj
def set_server_menu(ctx):
    """Set server commands"""


set_server_menu.add_command(set_server_locator_menu)
set_server_menu.add_command(set_server_os_image_command)
set_server_menu.add_command(set_server_power_menu)
set_server_menu.add_command(set_server_scu_command)
set_server_menu.add_command(set_server_tag_command)
