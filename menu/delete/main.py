import click

from menu.delete.aci.main import delete_aci_menu
from menu.delete.cvim.main import delete_cvim_menu
from menu.delete.helm.main import delete_helm_menu
from menu.delete.imc.main import delete_imc_menu
from menu.delete.intersight.main import delete_intersight_menu
from menu.delete.k8s.main import delete_k8s_menu
from menu.delete.linux.main import delete_linux_menu
from menu.delete.nso.main import delete_nso_menu
from menu.delete.nx.main import delete_nx_menu
from menu.delete.ocp.main import delete_ocp_menu
from menu.delete.osp.main import delete_osp_menu
from menu.delete.server.main import delete_server_menu
from menu.delete.ucsm.main import delete_ucsm_menu
from menu.delete.vc.main import delete_vc_menu


class Failure(Exception):
    pass


@click.group("delete")
@click.pass_obj
def delete_menu(ctx):
    """Delete commands"""


delete_menu.add_command(delete_aci_menu)
delete_menu.add_command(delete_cvim_menu)
delete_menu.add_command(delete_helm_menu)
delete_menu.add_command(delete_imc_menu)
delete_menu.add_command(delete_intersight_menu)
delete_menu.add_command(delete_k8s_menu)
delete_menu.add_command(delete_linux_menu)
delete_menu.add_command(delete_nso_menu)
delete_menu.add_command(delete_nx_menu)
delete_menu.add_command(delete_ocp_menu)
delete_menu.add_command(delete_osp_menu)
delete_menu.add_command(delete_server_menu)
delete_menu.add_command(delete_ucsm_menu)
delete_menu.add_command(delete_vc_menu)
