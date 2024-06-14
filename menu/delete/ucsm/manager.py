import sys
import traceback
import click

from lib.ucsm import settings

from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("manager")
@click.pass_obj
@click.option("--name", "ucsm_name", default='', help="UCSM name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_ucsm_manager_command(
        ctx,
        ucsm_name,
        devel
        ):
    """Delete ucsm manager information"""

    # iserver delete ucsm manager

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        settings_handler = settings.UcsmSettings(log_id=ctx.run_id)
        success = settings_handler.delete_ucsm_manager(
            ucsm_name,
        )
        if not success:
            ctx.my_output.error('Failed to delete ucsm entry')
            raise ErrorExit

        ctx.my_output.default('UCSM entry deleted: %s' % (ucsm_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
