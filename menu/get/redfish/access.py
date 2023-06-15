import sys
import json
import traceback
import click

from progress.bar import Bar

from lib.redfish import endpoint_settings

from menu import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("access")
@click.pass_obj
@click.option("--type", "endpoint_type", type=click.Choice(['', 'standard', 'ucsc', 'fi', 'dell', 'hpe'], case_sensitive=False), default='', help="Redfish endpoint type")
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip_subnet, help="Redfish management IP")
@click.option("--serial", "serial_number", default='', help="Endpoint serial number")
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify endpoint")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_redfish_access_command(
        ctx,
        endpoint_type,
        endpoint_ip,
        serial_number,
        show_password,
        verify,
        output,
        devel
        ):
    """Get redfish access configuration"""

    # iserver get redfish configuration

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
            log_id=ctx.run_id
        )
        endpoints = endpoint_settings_handler.get_redfish_endpoints_settings(
            endpoint_type=endpoint_type,
            endpoint_ip=endpoint_ip,
            serial_number=serial_number
        )

        if verify and len(endpoints) > 0:
            if output == 'default':
                bar_handler = Bar('Progress', max=len(endpoints))
                bar_handler.goto(0)

            for item in endpoints:
                item['endpoint']['verified'] = endpoint_settings_handler.verify_redfish_endpoint_authentication(
                    item['endpoint_id']
                )
                if output == 'default':
                    bar_handler.next()

            if output == 'default':
                bar_handler.finish()

        if not show_password:
            for item in endpoints:
                item['endpoint']['password'] = '******'

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    endpoints,
                    indent=4
                )
            )
            return

        if len(endpoints) == 0:
            ctx.my_output.default('No redfish endpoints found')
            return

        endpoint_settings_handler.print_redfish_endpoint_settings(
            endpoints,
            verify=verify
        )

        if verify:
            authenticated = 0
            for item in endpoints:
                if item['endpoint']['verified']:
                    authenticated = authenticated + 1

            ctx.my_output.default('\nAuthenticated: %s/%s' % (
                authenticated,
                len(endpoints)
            ))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
