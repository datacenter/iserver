import sys
import traceback
import click

from lib.aci import settings

from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("controller")
@click.pass_obj
@click.option("--name", "apic_name", default='', help="APIC name")
def delete_aci_controller_command(
        ctx,
        apic_name
        ):
    """Delete aci controller information"""

    # iserver delete aci controller

    ctx.developer = False
    common.flags_fixup(ctx, False, False, False)

    try:
        settings_handler = settings.ApicSettings(log_id=ctx.run_id)
        success = settings_handler.delete_apic_controller(
            apic_name,
        )
        if not success:
            ctx.my_output.error('Failed to delete apic entry')
            raise ErrorExit

        ctx.my_output.default('APIC entry deleted: %s' % (apic_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
