import click

from menu.get.ocp.vms.list import get_ocp_vms_list_command
from menu.get.ocp.vms.vol import get_ocp_vms_vol_command


class Failure(Exception):
    pass


@click.group("vms")
@click.pass_obj
def get_ocp_vms_menu(ctx):
    """Get ocp virtual machines commands"""


get_ocp_vms_menu.add_command(get_ocp_vms_list_command)
get_ocp_vms_menu.add_command(get_ocp_vms_vol_command)
