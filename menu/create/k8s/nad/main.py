import click

from menu.create.k8s.nad.bridge import create_k8s_nad_bridge_command
from menu.create.k8s.nad.ipvlan import create_k8s_nad_ipvlan_command
from menu.create.k8s.nad.macvlan import create_k8s_nad_macvlan_command
from menu.create.k8s.nad.vlan import create_k8s_nad_vlan_command


class Failure(Exception):
    pass


@click.group("nad")
@click.pass_obj
def create_k8s_nad_menu(ctx):
    """Create Kubernetes network attachment defitnion commands"""


create_k8s_nad_menu.add_command(create_k8s_nad_bridge_command)
create_k8s_nad_menu.add_command(create_k8s_nad_ipvlan_command)
create_k8s_nad_menu.add_command(create_k8s_nad_macvlan_command)
create_k8s_nad_menu.add_command(create_k8s_nad_vlan_command)
