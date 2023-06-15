import click

from menu.create.nso.nfvo.vnfd import create_nso_nfvo_vnfd_command
from menu.create.nso.nfvo.vnfi import create_nso_nfvo_vnfi_command


class Failure(Exception):
    pass


@click.group("nfvo")
@click.pass_obj
def create_nso_nfvo_menu(ctx):
    """Create nso nfvo commands"""


create_nso_nfvo_menu.add_command(create_nso_nfvo_vnfd_command)
create_nso_nfvo_menu.add_command(create_nso_nfvo_vnfi_command)
