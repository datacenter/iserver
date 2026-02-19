import click

from menu.delete.ocp.ai import delete_ocp_ai_command
from menu.delete.ocp.cert_manager import delete_ocp_cert_manager_command
from menu.delete.ocp.cli_web import delete_ocp_cli_web
from menu.delete.ocp.connector import delete_ocp_connector
from menu.delete.ocp.cilium.main import delete_ocp_cilium_menu
from menu.delete.ocp.cluster.main import delete_ocp_cluster_menu
from menu.delete.ocp.cnv import delete_ocp_cnv_command
from menu.delete.ocp.gpu import delete_ocp_gpu_command
from menu.delete.ocp.grafana import delete_ocp_grafana_command
from menu.delete.ocp.htpasswd import delete_ocp_htpasswd_command
from menu.delete.ocp.imm import delete_ocp_imm_command
from menu.delete.ocp.iotel import delete_ocp_iotel_command
from menu.delete.ocp.lso import delete_ocp_lso_command
from menu.delete.ocp.lvm import delete_ocp_lvm_command
from menu.delete.ocp.minio import delete_ocp_minio_command
from menu.delete.ocp.mtv import delete_ocp_mtv_command
from menu.delete.ocp.nfd import delete_ocp_nfd_command
from menu.delete.ocp.nim import delete_ocp_nim_command
from menu.delete.ocp.nmstate import delete_ocp_nmstate_command
from menu.delete.ocp.odf import delete_ocp_odf_command
from menu.delete.ocp.portworx import delete_ocp_portworx_command
from menu.delete.ocp.prometheus import delete_ocp_prometheus_command
from menu.delete.ocp.serverless import delete_ocp_serverless_command
from menu.delete.ocp.service_mesh import delete_ocp_service_mesh_command
from menu.delete.ocp.splunk import delete_ocp_splunk_command
from menu.delete.ocp.sriov import delete_ocp_sriov_command
from menu.delete.ocp.ssh import delete_ocp_ssh_command
from menu.delete.ocp.task import delete_ocp_task_command
from menu.delete.ocp.tetragon import delete_ocp_tetragon_command
from menu.delete.ocp.trident import delete_ocp_trident_command
from menu.delete.ocp.vm import delete_ocp_vm_command


class Failure(Exception):
    pass


@click.group("ocp")
@click.pass_obj
def delete_ocp_menu(ctx):
    """Delete OpenShift commands"""


delete_ocp_menu.add_command(delete_ocp_ai_command)
delete_ocp_menu.add_command(delete_ocp_cert_manager_command)
delete_ocp_menu.add_command(delete_ocp_cli_web)
delete_ocp_menu.add_command(delete_ocp_connector)
delete_ocp_menu.add_command(delete_ocp_cilium_menu)
delete_ocp_menu.add_command(delete_ocp_cluster_menu)
delete_ocp_menu.add_command(delete_ocp_cnv_command)
delete_ocp_menu.add_command(delete_ocp_gpu_command)
delete_ocp_menu.add_command(delete_ocp_grafana_command)
delete_ocp_menu.add_command(delete_ocp_htpasswd_command)
delete_ocp_menu.add_command(delete_ocp_imm_command)
delete_ocp_menu.add_command(delete_ocp_iotel_command)
delete_ocp_menu.add_command(delete_ocp_lso_command)
delete_ocp_menu.add_command(delete_ocp_lvm_command)
delete_ocp_menu.add_command(delete_ocp_minio_command)
delete_ocp_menu.add_command(delete_ocp_mtv_command)
delete_ocp_menu.add_command(delete_ocp_odf_command)
delete_ocp_menu.add_command(delete_ocp_nfd_command)
delete_ocp_menu.add_command(delete_ocp_nim_command)
delete_ocp_menu.add_command(delete_ocp_nmstate_command)
delete_ocp_menu.add_command(delete_ocp_portworx_command)
delete_ocp_menu.add_command(delete_ocp_prometheus_command)
delete_ocp_menu.add_command(delete_ocp_serverless_command)
delete_ocp_menu.add_command(delete_ocp_service_mesh_command)
delete_ocp_menu.add_command(delete_ocp_splunk_command)
delete_ocp_menu.add_command(delete_ocp_sriov_command)
delete_ocp_menu.add_command(delete_ocp_ssh_command)
delete_ocp_menu.add_command(delete_ocp_task_command)
delete_ocp_menu.add_command(delete_ocp_tetragon_command)
delete_ocp_menu.add_command(delete_ocp_trident_command)
delete_ocp_menu.add_command(delete_ocp_vm_command)
