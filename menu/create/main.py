import click

from menu.create.aci.main import create_aci_menu
from menu.create.helm.main import create_helm_menu
from menu.create.imc.main import create_imc_menu
from menu.create.intersight.main import create_intersight_menu
from menu.create.k8s.main import create_k8s_menu
from menu.create.md import create_md_command
from menu.create.nso.main import create_nso_menu
from menu.create.ocp.main import create_ocp_menu
from menu.create.osp.main import create_osp_menu
from menu.create.server.main import create_server_menu
from menu.create.vc.main import create_vc_menu


class Failure(Exception):
    pass


@click.group("create")
@click.pass_obj
def create_menu(ctx):
    """Create commands"""


create_menu.add_command(create_aci_menu)
create_menu.add_command(create_helm_menu)
create_menu.add_command(create_imc_menu)
create_menu.add_command(create_intersight_menu)
create_menu.add_command(create_k8s_menu)
create_menu.add_command(create_md_command)
create_menu.add_command(create_nso_menu)
create_menu.add_command(create_ocp_menu)
create_menu.add_command(create_osp_menu)
create_menu.add_command(create_server_menu)
create_menu.add_command(create_vc_menu)
