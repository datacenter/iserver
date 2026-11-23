import click

from menu.delete.ucsm.manager import delete_ucsm_manager_command


class Failure(Exception):
    pass


@click.group("ucsm")
@click.pass_obj
def delete_ucsm_menu(ctx):
    """Delete ucsm commands"""


delete_ucsm_menu.add_command(delete_ucsm_manager_command)
