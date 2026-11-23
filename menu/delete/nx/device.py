import sys
import traceback
import click

from lib.nexus import settings

from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("device")
@click.pass_obj
@click.option("--name", "device_name", default='', help="Nexus device name")
def delete_nx_device_command(
        ctx,
        device_name
        ):
    """Delete nexus device information"""

    # iserver delete nx device

    ctx.developer = False
    common.flags_fixup(ctx, False, False, False)

    try:
        settings_handler = settings.NexusSettings(log_id=ctx.run_id)
        success = settings_handler.delete_nexus_device(
            device_name
        )
        if not success:
            ctx.my_output.error('Failed to delete nexus device')
            raise ErrorExit

        ctx.my_output.default('Nexus device deleted: %s' % (device_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
