import sys
import traceback
import click

from lib.nexus import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("switch")
@click.pass_obj
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nexus_switch_command(
        ctx,
        show_password,
        devel
        ):
    """Get nexus switches"""

    # iserver get nexus switch

    ctx.developer = devel

    try:
        settings_handler = settings.NexusSettings(log_id=ctx.run_id)

        switches = settings_handler.get_nexus_switches()
        if switches is None:
            ctx.my_output.error('Failed to get Nexus switches')
            raise ErrorExit

        settings_handler.print_nexus_switches(
            switches,
            show_password=show_password
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
