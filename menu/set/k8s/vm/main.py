import click

from menu.set.k8s.vm.cpu import set_k8s_vm_cpu
from menu.set.k8s.vm.mem import set_k8s_vm_mem
from menu.set.k8s.vm.pause import set_k8s_vm_pause
from menu.set.k8s.vm.restart import set_k8s_vm_restart
from menu.set.k8s.vm.start import set_k8s_vm_start
from menu.set.k8s.vm.stop import set_k8s_vm_stop
from menu.set.k8s.vm.unpause import set_k8s_vm_unpause


class Failure(Exception):
    pass


@click.group("vm")
@click.pass_obj
def set_k8s_vm_menu(ctx):
    """Virtual Machine Actions and Settings"""


set_k8s_vm_menu.add_command(set_k8s_vm_cpu)
set_k8s_vm_menu.add_command(set_k8s_vm_mem)
set_k8s_vm_menu.add_command(set_k8s_vm_pause)
set_k8s_vm_menu.add_command(set_k8s_vm_restart)
set_k8s_vm_menu.add_command(set_k8s_vm_start)
set_k8s_vm_menu.add_command(set_k8s_vm_stop)
set_k8s_vm_menu.add_command(set_k8s_vm_unpause)
