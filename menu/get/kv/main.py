import click

from menu.get.kv.vm import get_kubevirt_vm_command
from menu.get.kv.vmi import get_kubevirt_vmi_command


class Failure(Exception):
    pass


@click.group("kv")
@click.pass_obj
def get_kv_menu(ctx):
    """Get kubevirt commands (alpha)"""


get_kv_menu.add_command(get_kubevirt_vm_command)
get_kv_menu.add_command(get_kubevirt_vmi_command)
