import click

from menu.get.osp.az import get_osp_az_command
from menu.get.osp.cluster import get_osp_cluster
from menu.get.osp.fip import get_osp_fip_command
from menu.get.osp.flv import get_osp_flv_command
from menu.get.osp.hv import get_osp_hv_command
from menu.get.osp.img import get_osp_img_command
from menu.get.osp.net import get_osp_net_command
from menu.get.osp.port import get_osp_port_command
from menu.get.osp.quota import get_osp_quota_command
from menu.get.osp.role import get_osp_role_command
from menu.get.osp.rtr import get_osp_rtr_command
from menu.get.osp.sg import get_osp_sg_command
from menu.get.osp.snap import get_osp_snap_command
from menu.get.osp.sub import get_osp_sub_command
from menu.get.osp.tenant import get_osp_tenant_command
from menu.get.osp.user import get_osp_user_command
from menu.get.osp.vm import get_osp_vm_command
from menu.get.osp.vol import get_osp_vol_command


class Failure(Exception):
    pass


@click.group("osp")
@click.pass_obj
def get_osp_menu(ctx):
    """Get osp commands"""


get_osp_menu.add_command(get_osp_az_command)
get_osp_menu.add_command(get_osp_cluster)
get_osp_menu.add_command(get_osp_fip_command)
get_osp_menu.add_command(get_osp_flv_command)
get_osp_menu.add_command(get_osp_hv_command)
get_osp_menu.add_command(get_osp_img_command)
get_osp_menu.add_command(get_osp_net_command)
get_osp_menu.add_command(get_osp_port_command)
get_osp_menu.add_command(get_osp_quota_command)
get_osp_menu.add_command(get_osp_role_command)
get_osp_menu.add_command(get_osp_rtr_command)
get_osp_menu.add_command(get_osp_sg_command)
get_osp_menu.add_command(get_osp_snap_command)
get_osp_menu.add_command(get_osp_sub_command)
get_osp_menu.add_command(get_osp_tenant_command)
get_osp_menu.add_command(get_osp_user_command)
get_osp_menu.add_command(get_osp_vm_command)
get_osp_menu.add_command(get_osp_vol_command)
