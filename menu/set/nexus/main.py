import click

from menu.set.nexus.switch import set_nexus_switch_command


class Failure(Exception):
    pass


@click.group("nexus")
@click.pass_obj
def set_nexus_menu(ctx):
    """Set nexus commands"""


set_nexus_menu.add_command(set_nexus_switch_command)
