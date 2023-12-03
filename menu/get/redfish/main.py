import click

from menu.get.redfish.cache import get_redfish_cache_command
from menu.get.redfish.endpoint import get_redfish_endpoint_command
from menu.get.redfish.template import get_redfish_template_command
from menu.get.redfish.uri import get_redfish_uri_command


class Failure(Exception):
    pass


@click.group("redfish")
@click.pass_obj
def get_redfish_menu(ctx):
    """Get redfish commands"""


get_redfish_menu.add_command(get_redfish_cache_command)
get_redfish_menu.add_command(get_redfish_endpoint_command)
get_redfish_menu.add_command(get_redfish_template_command)
get_redfish_menu.add_command(get_redfish_uri_command)
