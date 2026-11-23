import click

from menu.get.aci.contract.standard import get_aci_contract_standard_command
from menu.get.aci.contract.taboo import get_aci_contract_taboo_command
from menu.get.aci.contract.filter import get_aci_contract_filter_command


class Failure(Exception):
    pass


@click.group("contract")
@click.pass_obj
def get_aci_contract_menu(ctx):
    """Get aci contract commands"""


get_aci_contract_menu.add_command(get_aci_contract_standard_command)
get_aci_contract_menu.add_command(get_aci_contract_taboo_command)
get_aci_contract_menu.add_command(get_aci_contract_filter_command)
