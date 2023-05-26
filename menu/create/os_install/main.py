import click

from menu.create.os_install.embedded import create_os_install_embedded_command
from menu.create.os_install.dhcp import create_os_install_dhcp_command
from menu.create.os_install.static import create_os_install_static_command
from menu.create.os_install.batch import create_os_install_batch_command


class Failure(Exception):
    pass


@click.group("os-install")
@click.pass_obj
def create_os_install_menu(ctx):
    """Create os installation commands"""


create_os_install_menu.add_command(create_os_install_embedded_command)
create_os_install_menu.add_command(create_os_install_dhcp_command)
create_os_install_menu.add_command(create_os_install_static_command)
create_os_install_menu.add_command(create_os_install_batch_command)
