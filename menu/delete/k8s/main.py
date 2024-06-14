import click

from menu.delete.k8s.cluster import delete_k8s_cluster
from menu.delete.k8s.dv import delete_k8s_dv_command
from menu.delete.k8s.pvc import delete_k8s_pvc_command
from menu.delete.k8s.srnnp import delete_k8s_srnnp_command
from menu.delete.k8s.vm import delete_k8s_vm_command


class Failure(Exception):
    pass


@click.group("k8s")
@click.pass_obj
def delete_k8s_menu(ctx):
    """Delete k8s commands"""


delete_k8s_menu.add_command(delete_k8s_cluster)
delete_k8s_menu.add_command(delete_k8s_dv_command)
delete_k8s_menu.add_command(delete_k8s_pvc_command)
delete_k8s_menu.add_command(delete_k8s_srnnp_command)
delete_k8s_menu.add_command(delete_k8s_vm_command)
