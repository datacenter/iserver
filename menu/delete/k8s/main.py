import click

from menu.delete.k8s.cluster import delete_k8s_cluster
from menu.delete.k8s.bgp import delete_k8s_bgp_command
from menu.delete.k8s.dv import delete_k8s_dv_command
from menu.delete.k8s.gd import delete_k8s_gd_command
from menu.delete.k8s.group import delete_k8s_group_command
from menu.delete.k8s.image_stream import delete_k8s_is_command
from menu.delete.k8s.locv import delete_k8s_locv_command
from menu.delete.k8s.locvd import delete_k8s_locvd_command
from menu.delete.k8s.locvs import delete_k8s_locvs_command
from menu.delete.k8s.nad import delete_k8s_nad_command
from menu.delete.k8s.nncp import delete_k8s_nncp_command
from menu.delete.k8s.pod import delete_k8s_pod_command
from menu.delete.k8s.pvc import delete_k8s_pvc_command
from menu.delete.k8s.sec import delete_k8s_sec_command
from menu.delete.k8s.srnnp import delete_k8s_srnnp_command
from menu.delete.k8s.user import delete_k8s_user_command


class Failure(Exception):
    pass


@click.group("k8s")
@click.pass_obj
def delete_k8s_menu(ctx):
    """Delete k8s commands"""


delete_k8s_menu.add_command(delete_k8s_cluster)
delete_k8s_menu.add_command(delete_k8s_bgp_command)
delete_k8s_menu.add_command(delete_k8s_dv_command)
delete_k8s_menu.add_command(delete_k8s_gd_command)
delete_k8s_menu.add_command(delete_k8s_group_command)
delete_k8s_menu.add_command(delete_k8s_is_command)
delete_k8s_menu.add_command(delete_k8s_locv_command)
delete_k8s_menu.add_command(delete_k8s_locvd_command)
delete_k8s_menu.add_command(delete_k8s_locvs_command)
delete_k8s_menu.add_command(delete_k8s_nad_command)
delete_k8s_menu.add_command(delete_k8s_nncp_command)
delete_k8s_menu.add_command(delete_k8s_pod_command)
delete_k8s_menu.add_command(delete_k8s_pvc_command)
delete_k8s_menu.add_command(delete_k8s_sec_command)
delete_k8s_menu.add_command(delete_k8s_srnnp_command)
delete_k8s_menu.add_command(delete_k8s_user_command)
