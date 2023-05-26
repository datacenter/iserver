import click

from menu.get.vc.instance import get_vc_instance_command
from menu.get.vc.host.main import get_vc_host_menu
from menu.get.vc.hosts import get_vc_hosts_command
from menu.get.vc.vms import get_vc_vms_command


class Failure(Exception):
    pass


@click.group("vc")
@click.pass_obj
def get_vc_menu(ctx):
    """Get vcenter commands"""


get_vc_menu.add_command(get_vc_instance_command)
get_vc_menu.add_command(get_vc_host_menu)
get_vc_menu.add_command(get_vc_hosts_command)
get_vc_menu.add_command(get_vc_vms_command)
