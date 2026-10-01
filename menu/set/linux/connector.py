import sys
import click
from menu import validations
from lib.linux import settings
from lib.linux import output as linux_output


@click.command("connector")
@click.pass_obj
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Linux name")
@click.option("--ip", "linux_ip", default='', callback=validations.empty_string_to_none, help="IP/FQDN")
@click.option("--username", default='', callback=validations.empty_string_to_none, help="Username")
@click.option("--password", default='', callback=validations.empty_string_to_none, help="Password")
@click.option("--key", default='', callback=validations.validate_optional_file, help="SSH public key")
def set_linux_connector_command(
        ctx,
        name,
        linux_ip,
        username,
        password,
        key
    ):
    """Set linux connector"""

    if name is None:
        name = ctx.my_output.get_input('Connector name: ', empty_to_none=True)
        if name is None:
            sys.exit(1)

    if linux_ip is None:
        linux_ip = ctx.my_output.get_input('IP: ', empty_to_none=True)
        if linux_ip is None:
            sys.exit(1)

    if username is None:
        username = ctx.my_output.get_input('Username: ', empty_to_none=True)
        if username is None:
            sys.exit(1)

    if password is None and key is None:
        password = ctx.my_output.get_input('Password: ', empty_to_none=True)
        key = None
        if password is None:
            password = ctx.my_output.get_input('Key: ', empty_to_none=True)

        if password is None and key is None:
            sys.exit(1)

    linux_output_handler = linux_output.LinuxOutput(log_id=ctx.run_id)
    settings_handler = settings.LinuxSettings(log_id=ctx.run_id)

    if not settings_handler.set_linux_server(name, linux_ip, username, password=password, key_filename=key):
        ctx.my_output.error('Failed to set linux server entry')
        sys.exit(1)

    servers = settings_handler.get_linux_servers()
    linux_output_handler.print_linux_servers(
        servers,
        show_password=False
    )