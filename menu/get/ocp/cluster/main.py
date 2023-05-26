import click

from menu.get.ocp.cluster.cni import get_ocp_cluster_cni_command
from menu.get.ocp.cluster.cnv.main import get_ocp_cluster_cnv_menu
from menu.get.ocp.cluster.console import get_ocp_cluster_console_command
from menu.get.ocp.cluster.fabric import get_ocp_cluster_fabric_command
from menu.get.ocp.cluster.installer import get_ocp_cluster_installer_command
from menu.get.ocp.cluster.kc import get_ocp_cluster_kc_command
from menu.get.ocp.cluster.nodes.main import get_ocp_cluster_nodes_menu
from menu.get.ocp.cluster.node import get_ocp_cluster_node_command
from menu.get.ocp.cluster.pods import get_ocp_cluster_pods_command
from menu.get.ocp.cluster.pod import get_ocp_cluster_pod_command
from menu.get.ocp.cluster.server import get_ocp_cluster_server_command
from menu.get.ocp.cluster.servers import get_ocp_cluster_servers_command
from menu.get.ocp.cluster.services import get_ocp_cluster_services_command
from menu.get.ocp.cluster.service import get_ocp_cluster_service_command
from menu.get.ocp.cluster.summary import get_ocp_cluster_summary_command
from menu.get.ocp.cluster.vcenter import get_ocp_cluster_vcenter_command


class Failure(Exception):
    pass


@click.group("cluster")
@click.pass_obj
def get_ocp_cluster_menu(ctx):
    """Get ocp cluster commands"""


get_ocp_cluster_menu.add_command(get_ocp_cluster_cni_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_cnv_menu)
get_ocp_cluster_menu.add_command(get_ocp_cluster_console_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_fabric_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_installer_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_kc_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_nodes_menu)
get_ocp_cluster_menu.add_command(get_ocp_cluster_node_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_pods_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_pod_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_server_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_servers_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_services_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_service_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_summary_command)
get_ocp_cluster_menu.add_command(get_ocp_cluster_vcenter_command)
