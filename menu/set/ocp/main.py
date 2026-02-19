import click

from menu.set.ocp.cilium.main import set_ocp_cilium_menu
from menu.set.ocp.cluster.main import set_ocp_cluster_menu

from menu.set.ocp.ai import set_ocp_ai_command
from menu.set.ocp.bashrc import set_ocp_bashrc_command
from menu.set.ocp.cert_manager import set_ocp_cert_manager_command
from menu.set.ocp.cli_butane import set_ocp_cli_butane
from menu.set.ocp.cli_cilium import set_ocp_cli_cilium
from menu.set.ocp.cli_helm import set_ocp_cli_helm
from menu.set.ocp.cli_hubble import set_ocp_cli_hubble
from menu.set.ocp.cli_tridentctl import set_ocp_cli_tridentctl
from menu.set.ocp.cli_virtctl import set_ocp_cli_virtctl
from menu.set.ocp.cli_web import set_ocp_cli_web
from menu.set.ocp.cni import set_ocp_cni_command
from menu.set.ocp.cnv import set_ocp_cnv_command
from menu.set.ocp.connector import set_ocp_connector
from menu.set.ocp.console import set_ocp_console_command
from menu.set.ocp.file import set_ocp_file_command
from menu.set.ocp.gpu import set_ocp_gpu_command
from menu.set.ocp.grafana import set_ocp_grafana_command
from menu.set.ocp.htpasswd import set_ocp_htpasswd_command
from menu.set.ocp.imm import set_ocp_imm_command
from menu.set.ocp.iotel import set_ocp_iotel_command
from menu.set.ocp.lso import set_ocp_lso_command
from menu.set.ocp.lvm import set_ocp_lvm_command
from menu.set.ocp.minio import set_ocp_minio_command
from menu.set.ocp.mtv import set_ocp_mtv_command
from menu.set.ocp.node.main import set_ocp_node_menu
from menu.set.ocp.nfd import set_ocp_nfd_command
from menu.set.ocp.nim import set_ocp_nim_command
from menu.set.ocp.nfs import set_ocp_nfs_command
from menu.set.ocp.nmstate import set_ocp_nmstate_command
from menu.set.ocp.odf import set_ocp_odf_command
from menu.set.ocp.portworx import set_ocp_portworx_command
from menu.set.ocp.prometheus import set_ocp_prometheus_command
from menu.set.ocp.serverless import set_ocp_serverless_command
from menu.set.ocp.service_mesh import set_ocp_service_mesh_command
from menu.set.ocp.splunk import set_ocp_splunk_command
from menu.set.ocp.sriov import set_ocp_sriov_command
from menu.set.ocp.ssh import set_ocp_ssh_command
from menu.set.ocp.task import set_ocp_task_command
from menu.set.ocp.tetragon import set_ocp_tetragon_command
from menu.set.ocp.trident import set_ocp_trident_command


class Failure(Exception):
    pass


@click.group("ocp")
@click.pass_obj
def set_ocp_menu(ctx):
    """OCP Actions and Settings"""


set_ocp_menu.add_command(set_ocp_cluster_menu)
set_ocp_menu.add_command(set_ocp_cilium_menu)

set_ocp_menu.add_command(set_ocp_ai_command)
set_ocp_menu.add_command(set_ocp_bashrc_command)
set_ocp_menu.add_command(set_ocp_cert_manager_command)
set_ocp_menu.add_command(set_ocp_cli_butane)
set_ocp_menu.add_command(set_ocp_cli_cilium)
set_ocp_menu.add_command(set_ocp_cli_helm)
set_ocp_menu.add_command(set_ocp_cli_hubble)
set_ocp_menu.add_command(set_ocp_cli_tridentctl)
set_ocp_menu.add_command(set_ocp_cli_virtctl)
set_ocp_menu.add_command(set_ocp_cli_web)
set_ocp_menu.add_command(set_ocp_cni_command)
set_ocp_menu.add_command(set_ocp_cnv_command)
set_ocp_menu.add_command(set_ocp_connector)
set_ocp_menu.add_command(set_ocp_console_command)
set_ocp_menu.add_command(set_ocp_file_command)
set_ocp_menu.add_command(set_ocp_gpu_command)
set_ocp_menu.add_command(set_ocp_grafana_command)
set_ocp_menu.add_command(set_ocp_htpasswd_command)
set_ocp_menu.add_command(set_ocp_imm_command)
set_ocp_menu.add_command(set_ocp_iotel_command)
set_ocp_menu.add_command(set_ocp_lso_command)
set_ocp_menu.add_command(set_ocp_lvm_command)
set_ocp_menu.add_command(set_ocp_minio_command)
set_ocp_menu.add_command(set_ocp_mtv_command)
set_ocp_menu.add_command(set_ocp_node_menu)
set_ocp_menu.add_command(set_ocp_nfd_command)
set_ocp_menu.add_command(set_ocp_nim_command)
set_ocp_menu.add_command(set_ocp_nfs_command)
set_ocp_menu.add_command(set_ocp_nmstate_command)
set_ocp_menu.add_command(set_ocp_odf_command)
set_ocp_menu.add_command(set_ocp_portworx_command)
set_ocp_menu.add_command(set_ocp_prometheus_command)
set_ocp_menu.add_command(set_ocp_serverless_command)
set_ocp_menu.add_command(set_ocp_service_mesh_command)
set_ocp_menu.add_command(set_ocp_splunk_command)
set_ocp_menu.add_command(set_ocp_sriov_command)
set_ocp_menu.add_command(set_ocp_ssh_command)
set_ocp_menu.add_command(set_ocp_task_command)
set_ocp_menu.add_command(set_ocp_tetragon_command)
set_ocp_menu.add_command(set_ocp_trident_command)
