import click

from menu.delete.server.user import delete_server_user_command


class Failure(Exception):
    pass


@click.group("server")
@click.pass_obj
def delete_server_menu(ctx):
    """Create server commands"""


delete_server_menu.add_command(delete_server_user_command)
