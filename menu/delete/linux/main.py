import click

from menu.delete.linux.connector import delete_linux_connector_command
from menu.delete.linux.lvm import delete_linux_lvm_command


class Failure(Exception):
    pass


@click.group("linux")
@click.pass_obj
def delete_linux_menu(ctx):
    """Delete linux commands"""


delete_linux_menu.add_command(delete_linux_connector_command)
delete_linux_menu.add_command(delete_linux_lvm_command)