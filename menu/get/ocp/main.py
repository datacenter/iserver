import click

from menu.get.ocp.cluster.main import get_ocp_cluster_menu
from menu.get.ocp.clusters.main import get_ocp_clusters_menu
from menu.get.ocp.vm.main import get_ocp_vm_menu
from menu.get.ocp.vms.main import get_ocp_vms_menu
from menu.get.ocp.kc import get_ocp_clusters_kc_command
from menu.get.ocp.installer import get_ocp_installer_command
from menu.get.ocp.vcenter import get_ocp_vcenter_command


class Failure(Exception):
    pass


@click.group("ocp")
@click.pass_obj
def get_ocp_menu(ctx):
    """Get ocp commands"""


get_ocp_menu.add_command(get_ocp_cluster_menu)
get_ocp_menu.add_command(get_ocp_clusters_menu)
get_ocp_menu.add_command(get_ocp_vm_menu)
get_ocp_menu.add_command(get_ocp_vms_menu)
get_ocp_menu.add_command(get_ocp_clusters_kc_command)
get_ocp_menu.add_command(get_ocp_installer_command)
get_ocp_menu.add_command(get_ocp_vcenter_command)
