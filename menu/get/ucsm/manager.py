import sys
import traceback
import click

from lib.ucsm import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("manager")
@click.pass_obj
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ucsm_manager_command(
        ctx,
        show_password,
        devel
        ):
    """Get ucsm managers"""

    # iserver get ucsm manager

    ctx.developer = devel

    try:
        settings_handler = settings.UcsmSettings(log_id=ctx.run_id)

        managers = settings_handler.get_ucsm_managers()
        if managers is None:
            ctx.my_output.error('Failed to get UCSM managers')
            raise ErrorExit

        settings_handler.print_ucsm_managers(
            managers,
            show_password=show_password
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
