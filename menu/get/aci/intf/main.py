import click

from menu.get.aci.intf.cloudsec import get_aci_node_intf_cloudsec_command
from menu.get.aci.intf.fc import get_aci_node_intf_fc_command
from menu.get.aci.intf.fcpc import get_aci_node_intf_fcpc_command
from menu.get.aci.intf.l3e import get_aci_node_intf_l3e_command
from menu.get.aci.intf.lb import get_aci_node_intf_lb_command
from menu.get.aci.intf.macsec import get_aci_node_intf_macsec_command
from menu.get.aci.intf.mgmt import get_aci_node_intf_mgmt_command
from menu.get.aci.intf.pc import get_aci_node_intf_pc_command
from menu.get.aci.intf.phy import get_aci_node_intf_phy_command
from menu.get.aci.intf.summary import get_aci_node_intf_summary_command
from menu.get.aci.intf.svi import get_aci_node_intf_svi_command
from menu.get.aci.intf.tun import get_aci_node_intf_tun_command
from menu.get.aci.intf.vfc import get_aci_node_intf_vfc_command
from menu.get.aci.intf.vpc import get_aci_node_intf_vpc_command


class Failure(Exception):
    pass


@click.group("intf")
@click.pass_obj
def get_aci_node_intf_menu(ctx):
    """Get aci node interface commands"""


get_aci_node_intf_menu.add_command(get_aci_node_intf_cloudsec_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_fc_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_fcpc_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_l3e_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_lb_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_macsec_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_mgmt_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_pc_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_phy_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_summary_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_svi_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_tun_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_vfc_command)
get_aci_node_intf_menu.add_command(get_aci_node_intf_vpc_command)
