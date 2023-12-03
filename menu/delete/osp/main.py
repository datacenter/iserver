import click

from menu.delete.osp.cluster import delete_osp_cluster
from menu.delete.osp.vm import delete_osp_vm_command


class Failure(Exception):
    pass


@click.group("osp")
@click.pass_obj
def delete_osp_menu(ctx):
    """Delete osp commands"""


delete_osp_menu.add_command(delete_osp_cluster)
delete_osp_menu.add_command(delete_osp_vm_command)
