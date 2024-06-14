import click

from menu.get.nso.cnfd import get_nso_cnfd_command
from menu.get.nso.cnfi import get_nso_cnfi_command
from menu.get.nso.cnfm import get_nso_cnfm_command
from menu.get.nso.device import get_nso_device_command
from menu.get.nso.ncs import get_nso_ncs_command
from menu.get.nso.nfvo.main import get_nso_nfvo_menu


class Failure(Exception):
    pass


@click.group("nso")
@click.pass_obj
def get_nso_menu(ctx):
    """Get nso commands"""


get_nso_menu.add_command(get_nso_cnfd_command)
get_nso_menu.add_command(get_nso_cnfi_command)
get_nso_menu.add_command(get_nso_cnfm_command)
get_nso_menu.add_command(get_nso_device_command)
get_nso_menu.add_command(get_nso_ncs_command)
get_nso_menu.add_command(get_nso_nfvo_menu)
