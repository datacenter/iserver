import click

from menu.get.ocp.chrony import get_ocp_chrony_command
from menu.get.ocp.cpolicy import get_ocp_cpolicy_command
from menu.get.ocp.node import get_ocp_node_command
from menu.get.ocp.ssh import get_ocp_ssh_command
from menu.get.ocp.vm import get_ocp_vm_command


class Failure(Exception):
    pass


@click.group("ocp")
@click.pass_obj
def get_ocp_menu(ctx):
    """Get ocp commands"""


get_ocp_menu.add_command(get_ocp_chrony_command)
get_ocp_menu.add_command(get_ocp_cpolicy_command)
get_ocp_menu.add_command(get_ocp_node_command)
get_ocp_menu.add_command(get_ocp_ssh_command)
get_ocp_menu.add_command(get_ocp_vm_command)
