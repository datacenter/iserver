import sys
import traceback
import click

from menu import common

from lib.ucsm import manager
from lib.ucsm import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("manager")
@click.pass_obj
@click.option("--name", "ucsm_name", default='', help="UCSM name")
@click.option("--ip", "ucsm_ip", default='', help="UCSM IP/FQDN")
@click.option("--username", "ucsm_username", default='', help="UCSM username")
@click.option("--password", "ucsm_password", default='', help="UCSM password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_ucsm_manager_command(
        ctx,
        ucsm_name,
        ucsm_ip,
        ucsm_username,
        ucsm_password,
        devel
        ):
    """Set ucsm access details"""

    # iserver set ucsm manager

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        if len(ucsm_name) == 0:
            ctx.my_output.error('Define ucsm entry name')
            raise ErrorExit

        if len(ucsm_ip) == 0:
            ctx.my_output.error('Define ucsm ip address')
            raise ErrorExit

        if len(ucsm_username) == 0:
            ctx.my_output.error('Define ucsm username')
            raise ErrorExit

        if len(ucsm_password) == 0:
            ctx.my_output.error('Define ucsm password')
            raise ErrorExit

        ucsm_handler = manager.UcsManager(
            ucsm_ip,
            ucsm_username,
            ucsm_password,
            log_id=ctx.run_id
        )

        if not ucsm_handler.is_connected():
            ctx.my_output.error('Failed to connect to UCSM')
            raise ErrorExit

        ctx.my_output.default('UCSM authentication successful')

        settings_handler = settings.UcsmSettings(log_id=ctx.run_id)
        success = settings_handler.set_ucsm_manager(
            ucsm_name,
            ucsm_ip,
            ucsm_username,
            ucsm_password
        )
        if not success:
            ctx.my_output.error('Failed to define ucsm entry')
            raise ErrorExit

        ctx.my_output.default('UCSM entry created: %s' % (ucsm_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
