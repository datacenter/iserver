import click

from menu.get.aci.aaep import get_aci_aaep_command
from menu.get.aci.ap import get_aci_ap_command
from menu.get.aci.bd import get_aci_bd_command
from menu.get.aci.cache import get_aci_cache_command
from menu.get.aci.contract.main import get_aci_contract_menu
from menu.get.aci.controller import get_aci_controller_command
from menu.get.aci.domain.main import get_aci_domain_menu
from menu.get.aci.ep import get_aci_ep_command
from menu.get.aci.epg import get_aci_epg_command
from menu.get.aci.intf.main import get_aci_node_intf_menu
from menu.get.aci.l2out import get_aci_l2out_command
from menu.get.aci.l3out import get_aci_l3out_command
from menu.get.aci.mac import get_aci_mac_command
from menu.get.aci.mo import get_aci_mo_command
from menu.get.aci.node import get_aci_node_command
from menu.get.aci.pg.main import get_aci_pg_menu
from menu.get.aci.policy.main import get_aci_policy_menu
from menu.get.aci.pool.main import get_aci_pool_menu
from menu.get.aci.proto.main import get_aci_node_proto_menu
from menu.get.aci.psirt import get_aci_psirt_command
from menu.get.aci.system.main import get_aci_system_menu
from menu.get.aci.tenant import get_aci_tenant_command
from menu.get.aci.vrf import get_aci_vrf_command
from menu.get.aci.server import get_aci_server_command


class Failure(Exception):
    pass


@click.group("aci")
@click.pass_obj
def get_aci_menu(ctx):
    """Get aci commands"""


get_aci_menu.add_command(get_aci_aaep_command)
get_aci_menu.add_command(get_aci_epg_command)
get_aci_menu.add_command(get_aci_ap_command)
get_aci_menu.add_command(get_aci_bd_command)
get_aci_menu.add_command(get_aci_cache_command)
get_aci_menu.add_command(get_aci_contract_menu)
get_aci_menu.add_command(get_aci_controller_command)
get_aci_menu.add_command(get_aci_domain_menu)
get_aci_menu.add_command(get_aci_ep_command)
get_aci_menu.add_command(get_aci_node_intf_menu)
get_aci_menu.add_command(get_aci_l2out_command)
get_aci_menu.add_command(get_aci_l3out_command)
get_aci_menu.add_command(get_aci_mac_command)
get_aci_menu.add_command(get_aci_mo_command)
get_aci_menu.add_command(get_aci_node_command)
get_aci_menu.add_command(get_aci_pg_menu)
get_aci_menu.add_command(get_aci_policy_menu)
get_aci_menu.add_command(get_aci_pool_menu)
get_aci_menu.add_command(get_aci_psirt_command)
get_aci_menu.add_command(get_aci_node_proto_menu)
get_aci_menu.add_command(get_aci_system_menu)
get_aci_menu.add_command(get_aci_tenant_command)
get_aci_menu.add_command(get_aci_vrf_command)
get_aci_menu.add_command(get_aci_server_command)
