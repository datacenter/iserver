import click

from menu.get.linux.server import get_linux_server_command


class Failure(Exception):
    pass


@click.group("linux")
@click.pass_obj
def get_linux_menu(ctx):
    """Get linux commands"""


get_linux_menu.add_command(get_linux_server_command)
