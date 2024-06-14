import sys
import traceback
import click

from menu import common

from lib.nexus import nxapi
from lib.nexus import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("device")
@click.pass_obj
@click.option("--name", "nexus_name", default='', help="Nexus device name")
@click.option("--ip", "nexus_ip", default='', help="Nexus device IP/FQDN")
@click.option("--username", "nexus_username", default='', help="Nexus device username")
@click.option("--password", "nexus_password", default='', help="Nexus device password")
@click.option("--domain", "nexus_domain", default='', help="Administrative domain")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_nx_device_command(
        ctx,
        nexus_name,
        nexus_ip,
        nexus_username,
        nexus_password,
        nexus_domain,
        devel
        ):
    """Set nexus device access details"""

    # iserver set nx device

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        if len(nexus_name) == 0:
            ctx.my_output.error('Define nexus entry name')
            raise ErrorExit

        if len(nexus_ip) == 0:
            ctx.my_output.error('Define nexus ip address')
            raise ErrorExit

        if len(nexus_username) == 0:
            ctx.my_output.error('Define nexus username')
            raise ErrorExit

        if len(nexus_password) == 0:
            ctx.my_output.error('Define nexus password')
            raise ErrorExit

        nexus_handler = nxapi.NxApi(
            nexus_ip,
            nexus_username,
            nexus_password,
            name=nexus_name,
            log_id=ctx.run_id
        )

        nexus_handler.connect()
        if nexus_handler.is_connected():
            ctx.my_output.default('Nexus device authentication successful')
        else:
            ctx.my_output.error('Failed to connect to Nexus device. Continue?')
            if not common.get_confirmation():
                raise ErrorExit

        settings_handler = settings.NexusSettings(log_id=ctx.run_id)
        success = settings_handler.set_nexus_device(
            nexus_name,
            nexus_ip,
            nexus_username,
            nexus_password,
            domain=nexus_domain
        )
        if not success:
            ctx.my_output.error('Failed to define nexus entry')
            raise ErrorExit

        ctx.my_output.default('Nexus device entry created: %s' % (nexus_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
