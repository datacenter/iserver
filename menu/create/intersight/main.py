import click

from menu.create.intersight.os.main import create_intersight_os_menu
from menu.create.intersight.os_config import create_intersight_os_config_command
from menu.create.intersight.os_image import create_intersight_os_image_command
from menu.create.intersight.scu import create_intersight_scu_command


class Failure(Exception):
    pass


@click.group("is")
@click.pass_obj
def create_intersight_menu(ctx):
    """Create intersight commands"""


create_intersight_menu.add_command(create_intersight_os_menu)
create_intersight_menu.add_command(create_intersight_os_config_command)
create_intersight_menu.add_command(create_intersight_os_image_command)
create_intersight_menu.add_command(create_intersight_scu_command)
