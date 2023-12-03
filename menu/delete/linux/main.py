import click

from menu.delete.linux.server import delete_linux_server_command


class Failure(Exception):
    pass


@click.group("linux")
@click.pass_obj
def delete_linux_menu(ctx):
    """Delete linux commands"""


delete_linux_menu.add_command(delete_linux_server_command)
