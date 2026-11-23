import click

from menu.create.intersight.os.embedded import create_os_install_embedded_command
from menu.create.intersight.os.dhcp import create_os_install_dhcp_command
from menu.create.intersight.os.static import create_os_install_static_command
from menu.create.intersight.os.batch import create_os_install_batch_command
from menu.create.intersight.os.custom import create_os_install_custom_command


class Failure(Exception):
    pass


@click.group("os-install")
@click.pass_obj
def create_intersight_os_menu(ctx):
    """Run intersight OS installation commands"""


create_intersight_os_menu.add_command(create_os_install_embedded_command)
create_intersight_os_menu.add_command(create_os_install_dhcp_command)
create_intersight_os_menu.add_command(create_os_install_static_command)
create_intersight_os_menu.add_command(create_os_install_batch_command)
create_intersight_os_menu.add_command(create_os_install_custom_command)
