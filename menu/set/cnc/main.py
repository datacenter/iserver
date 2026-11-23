import click

from menu.set.cnc.controller import set_cnc_controller_command


class Failure(Exception):
    pass


@click.group("cnc")
@click.pass_obj
def set_cnc_menu(ctx):
    """Set cnc commands"""


set_cnc_menu.add_command(set_cnc_controller_command)
