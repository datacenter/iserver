import click

from menu.set.cvim.openrc import set_cvim_openrc


class Failure(Exception):
    pass


@click.group("cvim")
@click.pass_obj
def set_cvim_menu(ctx):
    """Cisco vim actions and settings"""


set_cvim_menu.add_command(set_cvim_openrc)
