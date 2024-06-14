import click

from menu.create.vc.vm import create_vc_vm_command


class Failure(Exception):
    pass


@click.group("vc")
@click.pass_obj
def create_vc_menu(ctx):
    """Create vCenter commands"""


create_vc_menu.add_command(create_vc_vm_command)
