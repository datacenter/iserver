import click

from menu.create.nso.nfvo.main import create_nso_nfvo_menu


class Failure(Exception):
    pass


@click.group("nso")
@click.pass_obj
def create_nso_menu(ctx):
    """Create nso commands"""


create_nso_menu.add_command(create_nso_nfvo_menu)
