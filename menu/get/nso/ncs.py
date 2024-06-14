import sys
import traceback
import click

from lib.nso import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ncs")
@click.pass_obj
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nso_ncs_command(
        ctx,
        show_password,
        devel
        ):
    """Get ncs instances"""

    # iserver get aci controller

    ctx.developer = devel

    try:
        settings_handler = settings.NsoSettings(log_id=ctx.run_id)

        ncss = settings_handler.get_nso_ncss()
        if ncss is None:
            ctx.my_output.error('Failed to get NSCs')
            raise ErrorExit

        settings_handler.print_nso_ncss(
            ncss,
            show_password=show_password
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
