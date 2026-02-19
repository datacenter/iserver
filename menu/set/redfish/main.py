import click

from menu.set.redfish.access.main import set_redfish_access_menu
from menu.set.redfish.bootoverride import set_redfish_boot_override_command
from menu.set.redfish.powercycle import set_redfish_power_cycle_command
from menu.set.redfish.poweron import set_redfish_power_on_command
from menu.set.redfish.poweroff import set_redfish_power_off_command
from menu.set.redfish.restart import set_redfish_restart_command
from menu.set.redfish.user import set_redfish_user_command
from menu.set.redfish.users import set_redfish_users_command
from menu.set.redfish.vmediaeject import set_redfish_vmedia_eject_command
from menu.set.redfish.vmediainsert import set_redfish_vmedia_insert_command


class Failure(Exception):
    pass


@click.group("redfish")
@click.pass_obj
def set_redfish_menu(ctx):
    """Set redfish commands"""


set_redfish_menu.add_command(set_redfish_access_menu)
set_redfish_menu.add_command(set_redfish_boot_override_command)
set_redfish_menu.add_command(set_redfish_power_cycle_command)
set_redfish_menu.add_command(set_redfish_power_on_command)
set_redfish_menu.add_command(set_redfish_power_off_command)
set_redfish_menu.add_command(set_redfish_restart_command)
set_redfish_menu.add_command(set_redfish_user_command)
set_redfish_menu.add_command(set_redfish_users_command)
set_redfish_menu.add_command(set_redfish_vmedia_eject_command)
set_redfish_menu.add_command(set_redfish_vmedia_insert_command)
