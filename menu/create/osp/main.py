import click

from menu.create.osp.fip import create_osp_fip_command
from menu.create.osp.flv import create_osp_flv_command
from menu.create.osp.img import create_osp_img_command
from menu.create.osp.net import create_osp_net_command
from menu.create.osp.rule import create_osp_rule_command
from menu.create.osp.sub import create_osp_subnet_command
from menu.create.osp.vm import create_osp_vm_command


class Failure(Exception):
    pass


@click.group("osp")
@click.pass_obj
def create_osp_menu(ctx):
    """Create OpenStack commands"""


create_osp_menu.add_command(create_osp_fip_command)
create_osp_menu.add_command(create_osp_flv_command)
create_osp_menu.add_command(create_osp_img_command)
create_osp_menu.add_command(create_osp_net_command)
create_osp_menu.add_command(create_osp_rule_command)
create_osp_menu.add_command(create_osp_subnet_command)
create_osp_menu.add_command(create_osp_vm_command)
