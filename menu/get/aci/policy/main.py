import click

from menu.get.aci.policy.auth import get_aci_policy_auth_command
from menu.get.aci.policy.cdp import get_aci_policy_cdp_command
from menu.get.aci.policy.copp import get_aci_policy_copp_command
from menu.get.aci.policy.dpp import get_aci_policy_dpp_command
from menu.get.aci.policy.drain import get_aci_policy_drain_command
from menu.get.aci.policy.fc import get_aci_policy_fc_command
from menu.get.aci.policy.flap import get_aci_policy_flap_command
from menu.get.aci.policy.l2 import get_aci_policy_l2_command
from menu.get.aci.policy.lacp import get_aci_policy_port_channel_command
from menu.get.aci.policy.lacp_member import get_aci_policy_port_channel_member_command
from menu.get.aci.policy.link import get_aci_policy_link_level_command
from menu.get.aci.policy.link_fc import get_aci_policy_link_level_fc_command
from menu.get.aci.policy.lldp import get_aci_policy_lldp_command
from menu.get.aci.policy.mcp import get_aci_policy_mcp_command
from menu.get.aci.policy.pfc import get_aci_policy_pfc_command
from menu.get.aci.policy.portsec import get_aci_policy_port_security_command
from menu.get.aci.policy.storm import get_aci_policy_storm_control_command
from menu.get.aci.policy.stp import get_aci_policy_stp_command
from menu.get.aci.policy.synce import get_aci_policy_synce_command
from menu.get.aci.policy.transceiver import get_aci_policy_transceiver_command


class Failure(Exception):
    pass


@click.group("policy")
@click.pass_obj
def get_aci_policy_menu(ctx):
    """Get aci policy commands"""


get_aci_policy_menu.add_command(get_aci_policy_auth_command)
get_aci_policy_menu.add_command(get_aci_policy_cdp_command)
get_aci_policy_menu.add_command(get_aci_policy_copp_command)
get_aci_policy_menu.add_command(get_aci_policy_dpp_command)
get_aci_policy_menu.add_command(get_aci_policy_drain_command)
get_aci_policy_menu.add_command(get_aci_policy_fc_command)
get_aci_policy_menu.add_command(get_aci_policy_flap_command)
get_aci_policy_menu.add_command(get_aci_policy_l2_command)
get_aci_policy_menu.add_command(get_aci_policy_link_level_command)
get_aci_policy_menu.add_command(get_aci_policy_link_level_fc_command)
get_aci_policy_menu.add_command(get_aci_policy_lldp_command)
get_aci_policy_menu.add_command(get_aci_policy_mcp_command)
get_aci_policy_menu.add_command(get_aci_policy_pfc_command)
get_aci_policy_menu.add_command(get_aci_policy_port_channel_command)
get_aci_policy_menu.add_command(get_aci_policy_port_channel_member_command)
get_aci_policy_menu.add_command(get_aci_policy_port_security_command)
get_aci_policy_menu.add_command(get_aci_policy_storm_control_command)
get_aci_policy_menu.add_command(get_aci_policy_stp_command)
get_aci_policy_menu.add_command(get_aci_policy_synce_command)
get_aci_policy_menu.add_command(get_aci_policy_transceiver_command)
