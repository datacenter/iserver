import sys
import traceback
import click

from menu import common

from lib.vc import vcenter
from lib.vc import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("instance")
@click.pass_obj
@click.option("--name", "vc_name", default='', help="vcenter name")
@click.option("--ip", "vc_ip", default='', help="vcenter IP/FQDN")
@click.option("--port", "vc_port", default=443, help="vcenter port")
@click.option("--username", "vc_username", default='', help="vcenter username")
@click.option("--password", "vc_password", default='', help="vcenter password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_vc_instance_command(
        ctx,
        vc_name,
        vc_ip,
        vc_port,
        vc_username,
        vc_password,
        devel
        ):
    """Set vcenter access details"""

    # iserver set vc instance

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        if len(vc_name) == 0:
            ctx.my_output.error('Define vcenter entry name')
            raise ErrorExit

        if len(vc_ip) == 0:
            ctx.my_output.error('Define vcenter ip address or name')
            raise ErrorExit

        if len(vc_username) == 0:
            ctx.my_output.error('Define vcenter username')
            raise ErrorExit

        if len(vc_password) == 0:
            ctx.my_output.error('Define vcenter password')
            raise ErrorExit

        vc_handler = vcenter.Vcenter(
            vc_ip,
            vc_username,
            vc_password,
            port=vc_port,
            log_id=ctx.run_id
        )

        if not vc_handler.is_vc_connected():
            raise ErrorExit

        ctx.my_output.default('vcenter authentication successful')

        settings_handler = settings.VcSettings(log_id=ctx.run_id)
        success = settings_handler.set_vc_instance(
            vc_name,
            vc_ip,
            vc_port,
            vc_username,
            vc_password
        )
        if not success:
            ctx.my_output.error('Failed to define vcenter entry')
            raise ErrorExit

        ctx.my_output.default('vcenter entry created: %s' % (vc_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
