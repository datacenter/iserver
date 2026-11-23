import click

from menu.set.linux.disk import set_linux_disk_command
from menu.set.linux.connector import set_linux_connector_command


class Failure(Exception):
    pass


@click.group("linux")
@click.pass_obj
def set_linux_menu(ctx):
    """Set linux commands"""


set_linux_menu.add_command(set_linux_connector_command)
set_linux_menu.add_command(set_linux_disk_command)
