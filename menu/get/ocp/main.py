import click

from menu.get.ocp.ai import get_ocp_ai_command
from menu.get.ocp.bashrc import get_ocp_bashrc_command
from menu.get.ocp.cert_manager import get_ocp_cert_manager_command
from menu.get.ocp.connector import get_ocp_connector
from menu.get.ocp.ntp import get_ocp_ntp_command
from menu.get.ocp.cilium.main import get_ocp_cilium_menu
from menu.get.ocp.cli_helm import get_ocp_cli_helm
from menu.get.ocp.cli_web import get_ocp_cli_web
from menu.get.ocp.cni import get_ocp_cni_command
from menu.get.ocp.cnv import get_ocp_cnv_command
from menu.get.ocp.cpolicy import get_ocp_cpolicy_command
from menu.get.ocp.fabric import get_ocp_cluster_fabric_command
from menu.get.ocp.gpu import get_ocp_gpu_command
from menu.get.ocp.grafana import get_ocp_grafana_command
from menu.get.ocp.htpasswd import get_ocp_htpasswd_command
from menu.get.ocp.imm import get_ocp_imm_command
from menu.get.ocp.iotel import get_ocp_iotel_command
from menu.get.ocp.lso import get_ocp_lso_command
from menu.get.ocp.lvm import get_ocp_lvm_command
from menu.get.ocp.minio import get_ocp_minio_command
from menu.get.ocp.mtv import get_ocp_mtv_command
from menu.get.ocp.nfd import get_ocp_nfd_command
from menu.get.ocp.nim import get_ocp_nim_command
from menu.get.ocp.nmstate import get_ocp_nmstate_command
from menu.get.ocp.odf import get_ocp_odf_command
from menu.get.ocp.portworx import get_ocp_portworx_command
from menu.get.ocp.prometheus import get_ocp_prometheus_command
from menu.get.ocp.serverless import get_ocp_serverless_command
from menu.get.ocp.service_mesh import get_ocp_service_mesh_command
from menu.get.ocp.splunk import get_ocp_splunk_command
from menu.get.ocp.sriov import get_ocp_sriov_command
from menu.get.ocp.ssh import get_ocp_ssh_command
from menu.get.ocp.tetragon import get_ocp_tetragon_command
from menu.get.ocp.trident import get_ocp_trident_command
from menu.get.ocp.vast import get_ocp_vast_command


class Failure(Exception):
    pass


@click.group("ocp")
@click.pass_obj
def get_ocp_menu(ctx):
    """Get ocp commands"""


get_ocp_menu.add_command(get_ocp_ai_command)
get_ocp_menu.add_command(get_ocp_bashrc_command)
get_ocp_menu.add_command(get_ocp_cert_manager_command)
get_ocp_menu.add_command(get_ocp_connector)
get_ocp_menu.add_command(get_ocp_ntp_command)
get_ocp_menu.add_command(get_ocp_cilium_menu)
get_ocp_menu.add_command(get_ocp_cli_helm)
get_ocp_menu.add_command(get_ocp_cli_web)
get_ocp_menu.add_command(get_ocp_cni_command)
get_ocp_menu.add_command(get_ocp_cnv_command)
get_ocp_menu.add_command(get_ocp_cpolicy_command)
get_ocp_menu.add_command(get_ocp_cluster_fabric_command)
get_ocp_menu.add_command(get_ocp_gpu_command)
get_ocp_menu.add_command(get_ocp_grafana_command)
get_ocp_menu.add_command(get_ocp_htpasswd_command)
get_ocp_menu.add_command(get_ocp_imm_command)
get_ocp_menu.add_command(get_ocp_iotel_command)
get_ocp_menu.add_command(get_ocp_lso_command)
get_ocp_menu.add_command(get_ocp_lvm_command)
get_ocp_menu.add_command(get_ocp_minio_command)
get_ocp_menu.add_command(get_ocp_mtv_command)
get_ocp_menu.add_command(get_ocp_nfd_command)
get_ocp_menu.add_command(get_ocp_nim_command)
get_ocp_menu.add_command(get_ocp_nmstate_command)
get_ocp_menu.add_command(get_ocp_odf_command)
get_ocp_menu.add_command(get_ocp_portworx_command)
get_ocp_menu.add_command(get_ocp_prometheus_command)
get_ocp_menu.add_command(get_ocp_serverless_command)
get_ocp_menu.add_command(get_ocp_service_mesh_command)
get_ocp_menu.add_command(get_ocp_splunk_command)
get_ocp_menu.add_command(get_ocp_sriov_command)
get_ocp_menu.add_command(get_ocp_ssh_command)
get_ocp_menu.add_command(get_ocp_tetragon_command)
get_ocp_menu.add_command(get_ocp_trident_command)
get_ocp_menu.add_command(get_ocp_vast_command)
