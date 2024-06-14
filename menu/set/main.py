import click

from menu.set.aci.main import set_aci_menu
from menu.set.cvim.main import set_cvim_menu
from menu.set.k8s.main import set_k8s_menu
from menu.set.linux.main import set_linux_menu
from menu.set.nx.main import set_nx_menu
from menu.set.nso.main import set_nso_menu
from menu.set.ocp.main import set_ocp_menu
from menu.set.osp.main import set_osp_menu
from menu.set.psirt import set_psirt_command
from menu.set.redfish.main import set_redfish_menu
from menu.set.server.main import set_server_menu
from menu.set.ucsm.main import set_ucsm_menu
from menu.set.vc.main import set_vc_menu


class Failure(Exception):
    pass


@click.group("set")
@click.pass_obj
def set_menu(ctx):
    """Actions and Settings"""


set_menu.add_command(set_aci_menu)
set_menu.add_command(set_cvim_menu)
set_menu.add_command(set_k8s_menu)
set_menu.add_command(set_linux_menu)
set_menu.add_command(set_nx_menu)
set_menu.add_command(set_nso_menu)
set_menu.add_command(set_ocp_menu)
set_menu.add_command(set_osp_menu)
set_menu.add_command(set_psirt_command)
set_menu.add_command(set_redfish_menu)
set_menu.add_command(set_server_menu)
set_menu.add_command(set_ucsm_menu)
set_menu.add_command(set_vc_menu)
