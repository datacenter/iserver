import sys
import traceback
import click

from lib.cnc import settings
from lib.cnc import output as cnc_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("controller")
@click.pass_obj
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_cnc_controller_command(
        ctx,
        show_password,
        devel
        ):
    """Get cnc controllers"""

    # iserver get cnc controller

    ctx.developer = devel

    try:
        settings_handler = settings.CncSettings(log_id=ctx.run_id)
        cnc_output_handler = cnc_output.CncOutput(log_id=ctx.run_id)

        controllers = settings_handler.get_cnc_controllers()
        if controllers is None:
            ctx.my_output.error('Failed to get CNC controllers')
            raise ErrorExit

        cnc_output_handler.print_cnc_controllers(
            controllers,
            show_password=show_password
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
