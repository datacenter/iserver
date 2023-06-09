import click

from menu.get.aci.main import get_aci_menu
from menu.get.intersight.main import get_intersight_menu
from menu.get.iwo.main import get_iwo_menu
from menu.get.nexus.main import get_nexus_menu
from menu.get.nso.main import get_nso_menu
from menu.get.ocp.main import get_ocp_menu
from menu.get.power import get_power_command
from menu.get.redfish.main import get_redfish_menu
from menu.get.thermal import get_thermal_command
from menu.get.ucsm.main import get_ucsm_menu
from menu.get.vc.main import get_vc_menu


class Failure(Exception):
    pass


@click.group("get")
@click.pass_obj
def get_menu(ctx):
    """Get commands"""


get_menu.add_command(get_aci_menu)
get_menu.add_command(get_intersight_menu)
get_menu.add_command(get_iwo_menu)
get_menu.add_command(get_nexus_menu)
get_menu.add_command(get_nso_menu)
get_menu.add_command(get_ocp_menu)
get_menu.add_command(get_power_command)
get_menu.add_command(get_redfish_menu)
get_menu.add_command(get_thermal_command)
get_menu.add_command(get_ucsm_menu)
get_menu.add_command(get_vc_menu)
