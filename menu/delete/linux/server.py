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
def delete_linux_server_command(
        ctx,
        name
        ):
    """Delete linux server"""

    # iserver delete linux server

    ctx.developer = False
    ctx.output = 'default'

    try:
        linux_output_handler = linux_output.LinuxOutput(log_id=ctx.run_id)
        settings_handler = settings.LinuxSettings(log_id=ctx.run_id)

        if settings_handler.get_linux_server(name) is None:
            ctx.my_output.error('Server %s not found' % (name))
            raise ErrorExit

        if not settings_handler.delete_linux_server(name):
            ctx.my_output.error('Server %s delete failed' % (name))
            raise ErrorExit

        ctx.my_output.default('Server %s deleted' % (name))
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
