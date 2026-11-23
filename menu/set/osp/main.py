import click

from menu.set.osp.openrc import set_osp_openrc


class Failure(Exception):
    pass


@click.group("osp")
@click.pass_obj
def set_osp_menu(ctx):
    """Openstack actions and settings"""


set_osp_menu.add_command(set_osp_openrc)
