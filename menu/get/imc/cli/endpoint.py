import sys
import json
import traceback
import click

from progress.bar import Bar

from lib import ip_helper
from lib.imc import settings
from lib.imc.cli import endpoint
from lib.imc.cli import output as imc_output

from menu import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("endpoint")
@click.pass_obj
@click.option("--ip", "endpoint_ip", multiple=True, callback=validations.validate_ips, help="IMC IP address")
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify endpoint")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_imc_cli_endpoint_command(
        ctx,
        endpoint_ip,
        show_password,
        verify,
        output,
        devel
        ):
    """Get imc endpoints"""

    # iserver get imc endpoint

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        endpoint_settings_handler = settings.ImcEndpointSettings(log_id=ctx.run_id)

        if len(endpoint_ip) > 0:
            endpoints = endpoint_settings_handler.get_cli_endpoints(
                ip_addresses=endpoint_ip
            )
        else:
            endpoints = endpoint_settings_handler.get_cli_endpoints()

        if endpoints is None:
            ctx.my_output.error('Failed to get imc endpoints')
            raise ErrorExit

        if verify and len(endpoints) > 0:
            if output == 'default':
                bar_handler = Bar('Progress', max=len(endpoints))
                bar_handler.goto(0)

            for item in endpoints:
                endpoint_handler = endpoint.ImcCliEndpoint(
                    item['ip'],
                    item['port'],
                    item['username'],
                    item['password'],
                    log_id=ctx.run_id
                )
                item['verified'] = endpoint_handler.is_cli_ready()
                if output == 'default':
                    bar_handler.next()

            if output == 'default':
                bar_handler.finish()

        if not show_password:
            for item in endpoints:
                item['password'] = '******'

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    endpoints,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(endpoints)

        if len(endpoints) == 0:
            ctx.my_output.default('No imc endpoints found')
            return

        output_handler = imc_output.ImcCliOutput(log_id=ctx.run_id)
        output_handler.print_imc_cli_endpoint_settings(
            endpoints,
            verify=verify,
            show_password=show_password
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
