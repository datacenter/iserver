import click

from menu.get.redfish.endpoint import get_redfish_endpoint_command
from menu.get.redfish.settings import get_redfish_settings_command
from menu.get.redfish.cache import get_redfish_cache_command
from menu.get.redfish.access import get_redfish_access_command
from menu.get.redfish.server import get_redfish_server_command
from menu.get.redfish.servers import get_redfish_servers_command
from menu.get.redfish.summary import get_redfish_summary_command


class Failure(Exception):
    pass


@click.group("redfish")
@click.pass_obj
def get_redfish_menu(ctx):
    """Get redfish commands"""


get_redfish_menu.add_command(get_redfish_endpoint_command)
get_redfish_menu.add_command(get_redfish_settings_command)
get_redfish_menu.add_command(get_redfish_cache_command)
get_redfish_menu.add_command(get_redfish_access_command)
get_redfish_menu.add_command(get_redfish_server_command)
get_redfish_menu.add_command(get_redfish_servers_command)
get_redfish_menu.add_command(get_redfish_summary_command)
