import sys
import threading
import traceback
import click

from progress.bar import Bar

from lib.redfish import endpoint_settings

from menu import common
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("access")
@click.pass_obj
@click.option("--type", "endpoint_type", type=click.Choice(['any', 'standard', 'ucsc', 'fi', 'dell', 'hpe'], case_sensitive=False), default='any', help="Redfish endpoint type")
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip_subnet, help="Redfish management IP")
@click.option("--serial", "serial_number", default='', help="Endpoint serial number")
@click.option("--failed", is_flag=True, show_default=True, default=False, help="Authentication failure")
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show redfish password")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_redfish_access_command(
        ctx,
        endpoint_type,
        endpoint_ip,
        serial_number,
        failed,
        show_password,
        devel
        ):
    """Delete redfish access information"""

    # iserver delete redfish access

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
            log_id=ctx.run_id
        )
        endpoints = endpoint_settings_handler.get_redfish_endpoints_settings(
            endpoint_type=endpoint_type,
            endpoint_ip=endpoint_ip,
            serial_number=serial_number
        )

        ctx.busy = False

        if len(endpoints) == 0:
            ctx.my_output.default('No redfish endpoints found')
            return

        if failed:
            failed_endpoints = []
            bar_handler = Bar('Progress', max=len(endpoints))
            bar_handler.goto(0)

            for item in endpoints:
                if not endpoint_settings_handler.verify_redfish_endpoint_authentication(item['endpoint_id']):
                    failed_endpoints.append(item)
                bar_handler.next()

            bar_handler.finish()

            if len(failed_endpoints) == 0:
                ctx.my_output.default('No redfish endpoints found')
                return

            endpoints = failed_endpoints

        endpoint_settings_handler.print_redfish_endpoint_settings(
            endpoints,
            show_password=show_password,
            verify=False
        )

        if common.get_confirmation():
            bar_handler = Bar('Progress', max=len(endpoints))
            bar_handler.goto(0)
            for item in endpoints:
                endpoint_settings_handler.delete_redfish_endpoint_settings(
                    item['endpoint_id']
                )
                bar_handler.next()

            bar_handler.finish()

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
