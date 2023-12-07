import sys
import traceback
import click

from menu import common

from lib.nso import settings
from lib.nso import main as nso


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ncs")
@click.pass_obj
@click.option("--name", "ncs_name", default='', help="NCS name")
@click.option("--ip", "ncs_ip", default='', help="NCS IP/FQDN")
@click.option("--username", "ncs_username", default='', help="NCS username")
@click.option("--password", "ncs_password", default='', help="NCS password")
@click.option("--port", "ncs_port", default=8080, help="NCS REST API Port")
@click.option("--nfvo", "nfvo_version", type=click.Choice(['none', '3.x', '4.x'], case_sensitive=False), default='none', show_default=True, help="NFVO Version")
@click.option("--protocol", "ncs_protocol", type=click.Choice(['http', 'https'], case_sensitive=False), default='http', show_default=True, help="Protocol")
@click.option("--restconf_disabled", is_flag=True, show_default=True, default=False, help="Restconf")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_nso_ncs_command(
        ctx,
        ncs_name,
        ncs_ip,
        ncs_username,
        ncs_password,
        ncs_port,
        nfvo_version,
        ncs_protocol,
        restconf_disabled,
        devel
        ):
    """Set nso ncs access details"""

    # iserver set nso ncs

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        if len(ncs_name) == 0:
            ctx.my_output.error('Define ncs entry name')
            raise ErrorExit

        if len(ncs_ip) == 0:
            ctx.my_output.error('Define ncs ip address')
            raise ErrorExit

        if len(ncs_username) == 0:
            ctx.my_output.error('Define ncs username')
            raise ErrorExit

        if len(ncs_password) == 0:
            ctx.my_output.error('Define ncs password')
            raise ErrorExit

        if nfvo_version == 'none':
            nfvo_version = None

        nso_handler = nso.Nso(
            ncs_protocol,
            ncs_ip,
            ncs_port,
            username=ncs_username,
            password=ncs_password,
            restconf_enabled=not restconf_disabled,
            nfvo=nfvo_version,
            log_id=ctx.run_id
        )

        if not nso_handler.is_connected():
            ctx.my_output.error('Failed to connect to NCS')
            raise ErrorExit

        ctx.my_output.default('NCS authentication successful')

        settings_handler = settings.NsoSettings(log_id=ctx.run_id)
        success = settings_handler.set_nso_ncs(
            ncs_name,
            ncs_protocol,
            ncs_ip,
            ncs_port,
            ncs_username,
            ncs_password,
            not restconf_disabled,
            nfvo_version
        )
        if not success:
            ctx.my_output.error('Failed to define ncs entry')
            raise ErrorExit

        ctx.my_output.default('NCS entry created: %s' % (ncs_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
