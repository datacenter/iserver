import click

from menu.get.nso.ncs import get_nso_ncs_command
from menu.get.nso.nfvo.main import get_nso_nfvo_menu


class Failure(Exception):
    pass


@click.group("nso")
@click.pass_obj
def get_nso_menu(ctx):
    """Get nso commands"""


get_nso_menu.add_command(get_nso_ncs_command)
get_nso_menu.add_command(get_nso_nfvo_menu)
