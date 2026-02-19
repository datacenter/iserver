import click

from menu.set.k8s.kc import set_k8s_kc
from menu.set.k8s.node.main import set_k8s_node_menu
from menu.set.k8s.sc.main import set_k8s_sc_menu
from menu.set.k8s.vm.main import set_k8s_vm_menu

class Failure(Exception):
    pass


@click.group("k8s")
@click.pass_obj
def set_k8s_menu(ctx):
    """K8s actions and settings"""


set_k8s_menu.add_command(set_k8s_kc)
set_k8s_menu.add_command(set_k8s_node_menu)
set_k8s_menu.add_command(set_k8s_sc_menu)
set_k8s_menu.add_command(set_k8s_vm_menu)
