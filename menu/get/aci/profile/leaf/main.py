import click

from menu.get.aci.profile.leaf.interface import get_aci_profile_leaf_interface_command


class Failure(Exception):
    pass


@click.group("leaf")
@click.pass_obj
def get_aci_profile_leaf_menu(ctx):
    """Get aci profile leaf commands"""


get_aci_profile_leaf_menu.add_command(get_aci_profile_leaf_interface_command)
