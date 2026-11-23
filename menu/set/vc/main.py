import click

from menu.set.vc.instance import set_vc_instance_command
from menu.set.vc.vm import set_vc_vm_command


class Failure(Exception):
    pass


@click.group("vc")
@click.pass_obj
def set_vc_menu(ctx):
    """Set vCenter commands"""


set_vc_menu.add_command(set_vc_instance_command)
set_vc_menu.add_command(set_vc_vm_command)
