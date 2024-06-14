import click

from menu.get.aci.main import get_aci_menu
from menu.get.chassis import get_chassis_command
from menu.get.cvim.main import get_cvim_menu
from menu.get.helm.main import get_helm_menu
from menu.get.intersight.main import get_intersight_menu
from menu.get.iwo.main import get_iwo_menu
from menu.get.k8s.main import get_k8s_menu
from menu.get.kv.main import get_kv_menu
from menu.get.linux.main import get_linux_menu
from menu.get.nc.main import get_nc_menu
from menu.get.nx.main import get_nx_menu
from menu.get.nso.main import get_nso_menu
from menu.get.ocp.main import get_ocp_menu
from menu.get.openshift.main import get_openshift_menu
from menu.get.osp.main import get_osp_menu
from menu.get.psirt import get_psirt_command
from menu.get.redfish.main import get_redfish_menu
from menu.get.server import get_server_command
from menu.get.ucsm.main import get_ucsm_menu
from menu.get.vc.main import get_vc_menu


class Failure(Exception):
    pass


@click.group("get")
@click.pass_obj
def get_menu(ctx):
    """Get commands"""


get_menu.add_command(get_aci_menu)
get_menu.add_command(get_chassis_command)
get_menu.add_command(get_cvim_menu)
get_menu.add_command(get_helm_menu)
get_menu.add_command(get_intersight_menu)
get_menu.add_command(get_iwo_menu)
get_menu.add_command(get_k8s_menu)
get_menu.add_command(get_kv_menu)
get_menu.add_command(get_linux_menu)
get_menu.add_command(get_nc_menu)
get_menu.add_command(get_nx_menu)
get_menu.add_command(get_nso_menu)
get_menu.add_command(get_ocp_menu)
get_menu.add_command(get_openshift_menu)
get_menu.add_command(get_osp_menu)
get_menu.add_command(get_psirt_command)
get_menu.add_command(get_redfish_menu)
get_menu.add_command(get_server_command)
get_menu.add_command(get_ucsm_menu)
get_menu.add_command(get_vc_menu)
