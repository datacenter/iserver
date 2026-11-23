import click

from menu.get.nc.notif import get_nc_notif_command


class Failure(Exception):
    pass


@click.group("nc")
@click.pass_obj
def get_nc_menu(ctx):
    """Get netconf commands"""


get_nc_menu.add_command(get_nc_notif_command)
