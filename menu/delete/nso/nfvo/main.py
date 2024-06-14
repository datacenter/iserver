import click

from menu.delete.nso.nfvo.vnfd import delete_nso_nfvo_vnfd_command
from menu.delete.nso.nfvo.vnfi import delete_nso_nfvo_vnfi_command


class Failure(Exception):
    pass


@click.group("nfvo")
@click.pass_obj
def delete_nso_nfvo_menu(ctx):
    """Delete nso nfvo commands"""


delete_nso_nfvo_menu.add_command(delete_nso_nfvo_vnfd_command)
delete_nso_nfvo_menu.add_command(delete_nso_nfvo_vnfi_command)
