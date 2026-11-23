import click

from menu.delete.vc.vm import delete_vc_vm_command


class Failure(Exception):
    pass


@click.group("vc")
@click.pass_obj
def delete_vc_menu(ctx):
    """Delete vCenter commands"""


delete_vc_menu.add_command(delete_vc_vm_command)
