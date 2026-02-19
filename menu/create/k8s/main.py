import click

from menu.create.k8s.dv import create_k8s_dv_command
from menu.create.k8s.nad.main import create_k8s_nad_menu
from menu.create.k8s.nncp import create_k8s_nncp_command
from menu.create.k8s.pvc import create_k8s_pvc_command
from menu.create.k8s.srnnp import create_k8s_srnnp_command
from menu.create.k8s.vm import create_k8s_vm_command


class Failure(Exception):
    pass


@click.group("k8s")
@click.pass_obj
def create_k8s_menu(ctx):
    """Create Kubernetes commands"""


create_k8s_menu.add_command(create_k8s_dv_command)
create_k8s_menu.add_command(create_k8s_nad_menu)
create_k8s_menu.add_command(create_k8s_nncp_command)
create_k8s_menu.add_command(create_k8s_pvc_command)
create_k8s_menu.add_command(create_k8s_srnnp_command)
create_k8s_menu.add_command(create_k8s_vm_command)
