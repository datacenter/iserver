import click

from menu.set.redfish.settings import set_redfish_settings_command
from menu.set.redfish.cache import set_redfish_cache_command
from menu.set.redfish.access.main import set_redfish_access_menu


class Failure(Exception):
    pass


@click.group("redfish")
@click.pass_obj
def set_redfish_menu(ctx):
    """Set redfish commands"""


set_redfish_menu.add_command(set_redfish_settings_command)
set_redfish_menu.add_command(set_redfish_cache_command)
set_redfish_menu.add_command(set_redfish_access_menu)
