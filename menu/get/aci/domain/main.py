import click

from menu.get.aci.domain.aaa import get_aci_domain_aaa_command
from menu.get.aci.domain.l2 import get_aci_domain_l2_command
from menu.get.aci.domain.l3 import get_aci_domain_l3_command
from menu.get.aci.domain.vmm import get_aci_domain_vmm_command
from menu.get.aci.domain.phy import get_aci_domain_phy_command


class Failure(Exception):
    pass


@click.group("domain")
@click.pass_obj
def get_aci_domain_menu(ctx):
    """Get aci domain commands"""


get_aci_domain_menu.add_command(get_aci_domain_aaa_command)
get_aci_domain_menu.add_command(get_aci_domain_l2_command)
get_aci_domain_menu.add_command(get_aci_domain_l3_command)
get_aci_domain_menu.add_command(get_aci_domain_vmm_command)
get_aci_domain_menu.add_command(get_aci_domain_phy_command)
