import click

from menu.delete.nso.nfvo.main import delete_nso_nfvo_menu


class Failure(Exception):
    pass


@click.group("nso")
@click.pass_obj
def delete_nso_menu(ctx):
    """Delete nso commands"""


delete_nso_menu.add_command(delete_nso_nfvo_menu)
