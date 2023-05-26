import click

from menu.set.ocp.vm.down import set_ocp_vm_down
from menu.set.ocp.vm.restart import set_ocp_vm_restart
from menu.set.ocp.vm.up import set_ocp_vm_up


class Failure(Exception):
    pass


@click.group("vm")
@click.pass_obj
def set_ocp_vm_menu(ctx):
    """OCP Virtual Machine Actions and Settings"""


set_ocp_vm_menu.add_command(set_ocp_vm_down)
set_ocp_vm_menu.add_command(set_ocp_vm_restart)
set_ocp_vm_menu.add_command(set_ocp_vm_up)
