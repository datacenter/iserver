import click

from menu.delete.osp.cluster import delete_osp_cluster
from menu.delete.osp.fip import delete_osp_fip_command
from menu.delete.osp.flv import delete_osp_flv_command
from menu.delete.osp.img import delete_osp_img_command
from menu.delete.osp.net import delete_osp_net_command
from menu.delete.osp.rule import delete_osp_rule_command
from menu.delete.osp.sub import delete_osp_sub_command
from menu.delete.osp.vm import delete_osp_vm_command


class Failure(Exception):
    pass


@click.group("osp")
@click.pass_obj
def delete_osp_menu(ctx):
    """Delete osp commands"""


delete_osp_menu.add_command(delete_osp_cluster)
delete_osp_menu.add_command(delete_osp_fip_command)
delete_osp_menu.add_command(delete_osp_flv_command)
delete_osp_menu.add_command(delete_osp_img_command)
delete_osp_menu.add_command(delete_osp_net_command)
delete_osp_menu.add_command(delete_osp_rule_command)
delete_osp_menu.add_command(delete_osp_sub_command)
delete_osp_menu.add_command(delete_osp_vm_command)
