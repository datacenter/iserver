import click

from menu.get.redfish.actions import get_redfish_actions_command
from menu.get.redfish.bios import get_redfish_bios_command
from menu.get.redfish.bootoverride import get_redfish_boot_override_command
from menu.get.redfish.fi import get_redfish_fi_command
from menu.get.redfish.power import get_redfish_power_command
from menu.get.redfish.template import get_redfish_template_command
from menu.get.redfish.uri import get_redfish_uri_command
from menu.get.redfish.vmedia import get_redfish_vmedia_command


class Failure(Exception):
    pass


@click.group("redfish")
@click.pass_obj
def get_redfish_menu(ctx):
    """Get redfish commands"""


get_redfish_menu.add_command(get_redfish_actions_command)
get_redfish_menu.add_command(get_redfish_bios_command)
get_redfish_menu.add_command(get_redfish_boot_override_command)
get_redfish_menu.add_command(get_redfish_fi_command)
get_redfish_menu.add_command(get_redfish_power_command)
get_redfish_menu.add_command(get_redfish_template_command)
get_redfish_menu.add_command(get_redfish_uri_command)
get_redfish_menu.add_command(get_redfish_vmedia_command)
