import click

from menu.set.linux.disk import set_linux_disk_command
from menu.set.linux.server import set_linux_server_command


class Failure(Exception):
    pass


@click.group("linux")
@click.pass_obj
def set_linux_menu(ctx):
    """Set linux commands"""


set_linux_menu.add_command(set_linux_disk_command)
set_linux_menu.add_command(set_linux_server_command)
