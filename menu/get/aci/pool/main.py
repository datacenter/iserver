import click

from menu.get.aci.pool.vlan import get_aci_pool_vlan_command


class Failure(Exception):
    pass


@click.group("pool")
@click.pass_obj
def get_aci_pool_menu(ctx):
    """Get aci pool commands"""


get_aci_pool_menu.add_command(get_aci_pool_vlan_command)
