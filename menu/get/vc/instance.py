import sys
import traceback
import click

from lib.vc import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("instance")
@click.pass_obj
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_vc_instance_command(
        ctx,
        show_password,
        devel
        ):
    """Get vcenter instances"""

    # iserver get vc instance

    ctx.developer = devel

    try:
        settings_handler = settings.VcSettings(log_id=ctx.run_id)

        instances = settings_handler.get_vc_instances()
        if instances is None:
            ctx.my_output.error('Failed to get vcenter instances')
            raise ErrorExit

        settings_handler.print_vc_instances(
            instances,
            show_password=show_password
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
