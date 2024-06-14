import click

from menu.create.helm.main import create_helm_menu
from menu.create.k8s.main import create_k8s_menu
from menu.create.nso.main import create_nso_menu
from menu.create.ocp.main import create_ocp_menu
from menu.create.osp.main import create_osp_menu
from menu.create.os_install.main import create_os_install_menu
from menu.create.os_image import create_os_image_command
from menu.create.server.main import create_server_menu
from menu.create.scu import create_scu_command
from menu.create.vc.main import create_vc_menu


class Failure(Exception):
    pass


@click.group("create")
@click.pass_obj
def create_menu(ctx):
    """Create commands"""


create_menu.add_command(create_helm_menu)
create_menu.add_command(create_k8s_menu)
create_menu.add_command(create_nso_menu)
create_menu.add_command(create_ocp_menu)
create_menu.add_command(create_osp_menu)
create_menu.add_command(create_os_install_menu)
create_menu.add_command(create_os_image_command)
create_menu.add_command(create_server_menu)
create_menu.add_command(create_scu_command)
create_menu.add_command(create_vc_menu)
