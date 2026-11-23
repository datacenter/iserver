import click

from menu.set.nso.ncs import set_nso_ncs_command


class Failure(Exception):
    pass


@click.group("nso")
@click.pass_obj
def set_nso_menu(ctx):
    """Set nso commands"""


set_nso_menu.add_command(set_nso_ncs_command)
