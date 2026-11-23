import click

from menu.get.aci.profile.leaf.main import get_aci_profile_leaf_menu


class Failure(Exception):
    pass


@click.group("profile")
@click.pass_obj
def get_aci_profile_menu(ctx):
    """Get aci profile commands"""


get_aci_profile_menu.add_command(get_aci_profile_leaf_menu)
