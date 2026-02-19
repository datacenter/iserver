import sys
import traceback
import click

from lib.imc import settings

from menu import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("endpoint")
@click.pass_obj
@click.option("--ip", "endpoint_ip", multiple=True, callback=validations.validate_ips, help="Management IP address")
@click.option("--port", "endpoint_port", default=22, help="IMC port")
@click.option("--username", default='', help="IMC ssh username")
@click.option("--password", default='', help="IMC ssh password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_imc_cli_endpoint_command(
        ctx,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        devel
        ):
    """Set imc cli access"""

    # iserver set imc cli endpoint

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        if len(endpoint_ip) == 0:
            ctx.my_output.error('Define IMC IP address(es)')
            raise ErrorExit

        if username == '':
            ctx.my_output.error('Define IMC ssh access username')
            raise ErrorExit

        if password == '':
            ctx.my_output.error('Define IMC ssh access password')
            raise ErrorExit

        endpoint_settings_handler = settings.ImcEndpointSettings(log_id=ctx.run_id)
        for ip_address in endpoint_ip:
            success = endpoint_settings_handler.set_imc_ssh_access(
                ip_address,
                username,
                password,
                port=endpoint_port
            )
            if not success:
                ctx.my_output.error('Failed to set IMC access for endpoint: %s' % (ip_address))
                raise ErrorExit

            ctx.my_output.default('IMC access configured for %s' % (ip_address))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
