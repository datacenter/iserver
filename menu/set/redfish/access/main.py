import click

from menu.set.redfish.access.fi import set_redfish_access_fi_command
from menu.set.redfish.access.servers import set_redfish_access_servers_command


class Failure(Exception):
    pass


@click.group("access")
@click.pass_obj
def set_redfish_access_menu(ctx):
    """Set redfish access commands"""


set_redfish_access_menu.add_command(set_redfish_access_fi_command)
set_redfish_access_menu.add_command(set_redfish_access_servers_command)
