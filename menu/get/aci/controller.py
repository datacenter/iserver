import sys
import traceback
import click

from lib.aci import settings
from lib.aci import output as aci_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("controller")
@click.pass_obj
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_controller_command(
        ctx,
        show_password,
        devel
        ):
    """Get aci controllers"""

    # iserver get aci controller

    ctx.developer = devel

    try:
        settings_handler = settings.ApicSettings(log_id=ctx.run_id)
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)

        controllers = settings_handler.get_apic_controllers()
        if controllers is None:
            ctx.my_output.error('Failed to get ACI controllers')
            raise ErrorExit

        aci_output_handler.print_apic_controllers(
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
