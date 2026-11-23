import click

from menu.get.aci.proto.arp import get_aci_node_proto_arp_command
from menu.get.aci.proto.bfd import get_aci_node_proto_bfd_command
from menu.get.aci.proto.bgp import get_aci_node_proto_bgp_command
from menu.get.aci.proto.cdp import get_aci_node_proto_cdp_command
from menu.get.aci.proto.hsrp import get_aci_node_proto_hsrp_command
from menu.get.aci.proto.ipv4 import get_aci_node_proto_ipv4_command
from menu.get.aci.proto.ipv6 import get_aci_node_proto_ipv6_command
from menu.get.aci.proto.isis import get_aci_node_proto_isis_command
from menu.get.aci.proto.lacp import get_aci_node_proto_lacp_command
from menu.get.aci.proto.lldp import get_aci_node_proto_lldp_command
from menu.get.aci.proto.nd import get_aci_node_proto_nd_command


class Failure(Exception):
    pass


@click.group("proto")
@click.pass_obj
def get_aci_node_proto_menu(ctx):
    """Get aci node protocol commands"""


get_aci_node_proto_menu.add_command(get_aci_node_proto_arp_command)
get_aci_node_proto_menu.add_command(get_aci_node_proto_bfd_command)
get_aci_node_proto_menu.add_command(get_aci_node_proto_bgp_command)
get_aci_node_proto_menu.add_command(get_aci_node_proto_cdp_command)
get_aci_node_proto_menu.add_command(get_aci_node_proto_hsrp_command)
get_aci_node_proto_menu.add_command(get_aci_node_proto_ipv4_command)
get_aci_node_proto_menu.add_command(get_aci_node_proto_ipv6_command)
get_aci_node_proto_menu.add_command(get_aci_node_proto_isis_command)
get_aci_node_proto_menu.add_command(get_aci_node_proto_lacp_command)
get_aci_node_proto_menu.add_command(get_aci_node_proto_lldp_command)
get_aci_node_proto_menu.add_command(get_aci_node_proto_nd_command)
