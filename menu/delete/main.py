import click

from menu.delete.aci.main import delete_aci_menu
from menu.delete.nso.main import delete_nso_menu
from menu.delete.ocp.main import delete_ocp_menu
from menu.delete.os_image import delete_os_image_command
from menu.delete.redfish.main import delete_redfish_menu
from menu.delete.scu import delete_scu_command
from menu.delete.ucsm.main import delete_ucsm_menu


class Failure(Exception):
    pass


@click.group("delete")
@click.pass_obj
def delete_menu(ctx):
    """Delete commands"""


delete_menu.add_command(delete_aci_menu)
delete_menu.add_command(delete_nso_menu)
delete_menu.add_command(delete_ocp_menu)
delete_menu.add_command(delete_os_image_command)
delete_menu.add_command(delete_redfish_menu)
delete_menu.add_command(delete_scu_command)
delete_menu.add_command(delete_ucsm_menu)
