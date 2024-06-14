import sys
import traceback
import click

from menu import validations

from lib.linux import settings
from lib.linux import output as linux_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("server")
@click.pass_obj
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Linux name")
@click.option("--ip", "linux_ip", default='', callback=validations.empty_string_to_none, help="IP/FQDN")
@click.option("--username", default='', callback=validations.empty_string_to_none, help="Username")
@click.option("--password", default='', callback=validations.empty_string_to_none, help="Password")
@click.option("--key", default='', callback=validations.validate_optional_file, help="SSH public key")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_linux_server_command(
        ctx,
        name,
        linux_ip,
        username,
        password,
        key,
        devel
        ):
    """Set linux server access details"""

    # iserver set linux server

    ctx.developer = devel
    ctx.output = 'default'

    try:
        if name is None:
            ctx.my_output.error('Define linux server entry name')
            raise ErrorExit

        if linux_ip is None:
            ctx.my_output.error('Define linux server ip address')
            raise ErrorExit

        if username is None:
            ctx.my_output.error('Define username')
            raise ErrorExit

        if password is None and key is None:
            ctx.my_output.error('Define password or public key')
            raise ErrorExit

        if password is not None and key is not None:
            ctx.my_output.error('Define password or public key')
            raise ErrorExit

        linux_output_handler = linux_output.LinuxOutput(log_id=ctx.run_id)
        settings_handler = settings.LinuxSettings(log_id=ctx.run_id)

        if not settings_handler.set_linux_server(name, linux_ip, username, password=password, key_filename=key):
            ctx.my_output.error('Failed to set linux server entry')
            raise ErrorExit

        servers = settings_handler.get_linux_servers()
        linux_output_handler.print_linux_servers(
            servers,
            show_password=False
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
