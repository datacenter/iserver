import click

from menu.get.linux.bond import get_linux_bond_command
from menu.get.linux.boot import get_linux_boot_command
from menu.get.linux.hp import get_linux_hp_command
from menu.get.linux.server import get_linux_server_command
from menu.get.linux.sysctl import get_linux_sysctl_command


class Failure(Exception):
    pass


@click.group("linux")
@click.pass_obj
def get_linux_menu(ctx):
    """Get linux commands"""


get_linux_menu.add_command(get_linux_bond_command)
get_linux_menu.add_command(get_linux_boot_command)
get_linux_menu.add_command(get_linux_hp_command)
get_linux_menu.add_command(get_linux_server_command)
get_linux_menu.add_command(get_linux_sysctl_command)
