import sys
import json
import threading
import traceback
import click

from lib.netconf import notification

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("notif")
@click.pass_obj
@click.option("--ip", "netconf_ip", default='', callback=validations.validate_ip, help="Netconf IP")
@click.option("--username", "netconf_username", default='', help="Netconf Username")
@click.option("--password", "netconf_password", default='', help="Netconf Password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nc_notif_command(
        ctx,
        netconf_ip,
        netconf_username,
        netconf_password,
        devel
        ):
    """Get netconf notification"""

    # iserver get vc vms

    ctx.developer = devel
    ctx.output = 'default'

    try:
        netconf_ip = '10.58.28.230'
        netconf_port = 2022
        netconf_username = 'admin'
        netconf_password = 'admin'

        notif_handler = notification.NetconfNotification(
            netconf_ip,
            netconf_port,
            netconf_username,
            netconf_password,
            log_id=ctx.run_id
        )

        if not notif_handler.is_working():
            ctx.my_output.error('Netconf connection failed')
            raise ErrorExit

        ctx.my_output.default('Netconf connection working')

        stream = 'ncs-events'
        if not notif_handler.is_stream(stream):
            ctx.my_output.error('Stream connection failed: %s' % (stream))
            raise ErrorExit

        ctx.my_output.default('Stream working: %s' % (stream))

        notif_handler.get_notifications(stream)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
