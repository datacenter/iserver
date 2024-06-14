import sys
import traceback
import click

from lib.linux import settings
from lib.linux import output as linux_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("server")
@click.pass_obj
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_linux_server_command(
        ctx,
        show_password,
        output,
        devel
        ):
    """Get linux servers"""

    # iserver get linux server

    ctx.developer = devel
    ctx.output = output

    try:
        linux_output_handler = linux_output.LinuxOutput(log_id=ctx.run_id)
        settings_handler = settings.LinuxSettings(log_id=ctx.run_id)

        servers = settings_handler.get_linux_servers()
        if servers is None:
            ctx.my_output.error('Failed to get linux servers')
            raise ErrorExit

        linux_output_handler.print_linux_servers(
            servers,
            show_password=show_password
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
