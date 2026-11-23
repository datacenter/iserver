import click

from menu.get.vc.host.pnet import get_vc_host_pnet_command


class Failure(Exception):
    pass


@click.group("host")
@click.pass_obj
def get_vc_host_menu(ctx):
    """Get vcenter host commands"""


get_vc_host_menu.add_command(get_vc_host_pnet_command)
