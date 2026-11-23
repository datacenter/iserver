import click

from menu.set.server.power.on import set_server_power_on_command
from menu.set.server.power.off import set_server_power_off_command
from menu.set.server.power.cycle import set_server_power_cycle_command
from menu.set.server.power.hard import set_server_power_hard_command
from menu.set.server.power.shut import set_server_power_shut_command
from menu.set.server.power.reboot import set_server_power_reboot_command


class Failure(Exception):
    pass


@click.group("power")
@click.pass_obj
def set_server_power_menu(ctx):
    """Set server power commands"""


set_server_power_menu.add_command(set_server_power_on_command)
set_server_power_menu.add_command(set_server_power_off_command)
set_server_power_menu.add_command(set_server_power_cycle_command)
set_server_power_menu.add_command(set_server_power_hard_command)
set_server_power_menu.add_command(set_server_power_shut_command)
set_server_power_menu.add_command(set_server_power_reboot_command)
