import click

from menu.get.nso.nfvo.vnfd import get_nso_nfvo_vnfd_command
from menu.get.nso.nfvo.vnfi import get_nso_nfvo_vnfi_command


class Failure(Exception):
    pass


@click.group("nfvo")
@click.pass_obj
def get_nso_nfvo_menu(ctx):
    """Get nso nfvo commands"""


get_nso_nfvo_menu.add_command(get_nso_nfvo_vnfd_command)
get_nso_nfvo_menu.add_command(get_nso_nfvo_vnfi_command)
