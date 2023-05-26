import click

from menu.get.ocp.vm.access import get_ocp_vm_access_command
from menu.get.ocp.vm.disk import get_ocp_vm_disk_command
from menu.get.ocp.vm.file import get_ocp_vm_file_command
from menu.get.ocp.vm.net import get_ocp_vm_net_command
from menu.get.ocp.vm.report import get_ocp_vm_report_command
from menu.get.ocp.vm.summary import get_ocp_vm_summary_command


class Failure(Exception):
    pass


@click.group("vm")
@click.pass_obj
def get_ocp_vm_menu(ctx):
    """Get ocp virtual machine commands"""


get_ocp_vm_menu.add_command(get_ocp_vm_access_command)
get_ocp_vm_menu.add_command(get_ocp_vm_disk_command)
get_ocp_vm_menu.add_command(get_ocp_vm_file_command)
get_ocp_vm_menu.add_command(get_ocp_vm_net_command)
get_ocp_vm_menu.add_command(get_ocp_vm_report_command)
get_ocp_vm_menu.add_command(get_ocp_vm_summary_command)
