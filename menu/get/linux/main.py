import click

from menu.get.linux.bond import get_linux_bond_command
from menu.get.linux.boot import get_linux_boot_command
from menu.get.linux.hp import get_linux_hp_command
from menu.get.linux.lsblk import get_linux_lsblk_command
from menu.get.linux.lv import get_linux_lv_command
from menu.get.linux.lvm import get_linux_lvm_command
from menu.get.linux.pv import get_linux_pv_command
from menu.get.linux.server import get_linux_server_command
from menu.get.linux.sysctl import get_linux_sysctl_command
from menu.get.linux.vg import get_linux_vg_command


class Failure(Exception):
    pass


@click.group("linux")
@click.pass_obj
def get_linux_menu(ctx):
    """Get linux commands"""


get_linux_menu.add_command(get_linux_bond_command)
get_linux_menu.add_command(get_linux_boot_command)
get_linux_menu.add_command(get_linux_hp_command)
get_linux_menu.add_command(get_linux_lsblk_command)
get_linux_menu.add_command(get_linux_lv_command)
get_linux_menu.add_command(get_linux_lvm_command)
get_linux_menu.add_command(get_linux_pv_command)
get_linux_menu.add_command(get_linux_server_command)
get_linux_menu.add_command(get_linux_sysctl_command)
get_linux_menu.add_command(get_linux_vg_command)
