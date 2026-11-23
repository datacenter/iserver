import click

from menu.create.server.user import create_server_user_command


class Failure(Exception):
    pass


@click.group("server")
@click.pass_obj
def create_server_menu(ctx):
    """Create server commands"""


create_server_menu.add_command(create_server_user_command)
