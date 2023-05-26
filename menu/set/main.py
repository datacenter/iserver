import click

from menu.set.aci.main import set_aci_menu
from menu.set.nexus.main import set_nexus_menu
from menu.set.nso.main import set_nso_menu
from menu.set.ocp.main import set_ocp_menu
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
set_menu.add_command(set_nexus_menu)
set_menu.add_command(set_nso_menu)
set_menu.add_command(set_ocp_menu)
set_menu.add_command(set_redfish_menu)
set_menu.add_command(set_server_menu)
set_menu.add_command(set_ucsm_menu)
set_menu.add_command(set_vc_menu)
