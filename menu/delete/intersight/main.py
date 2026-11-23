import click

from menu.delete.intersight.os_config import delete_intersight_os_config_command
from menu.delete.intersight.os_image import delete_intersight_os_image_command
from menu.delete.intersight.scu import delete_intersight_scu_command


class Failure(Exception):
    pass


@click.group("is")
@click.pass_obj
def delete_intersight_menu(ctx):
    """Delete intersight commands"""


delete_intersight_menu.add_command(delete_intersight_os_config_command)
delete_intersight_menu.add_command(delete_intersight_os_image_command)
delete_intersight_menu.add_command(delete_intersight_scu_command)
