import sys
import json
import threading
import traceback
import click

from lib.redfish import endpoint
from lib.redfish import endpoint_settings
from lib.redfish import output as redfish_output
from lib import ip_helper

from menu import common
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("fi")
@click.pass_obj
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def get_redfish_fi_command(
        ctx,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        output
        ):
    """Get redfish fi resources"""

    ctx.developer = False

    try:
        common.flags_fixup(ctx, False, False, False)

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        redfish_handler = endpoint.RedfishEndpoint(
            'fi',
            endpoint_ip,
            endpoint_port,
            username,
            password,
            auto_connect=True,
            ssl_verify=False,
            log_id=ctx.run_id
        )

        if not redfish_handler.is_connected():
            ctx.busy = False
            ctx.my_output.error(
                'Redfish access failed'
            )
            raise ErrorExit

        inventory = redfish_handler.endpoint_handler.get_inventory()

        ctx.busy = False

        output_handler = redfish_output.RedfishOutput(log_id=ctx.run_id)
        output_handler.print_inventory_chassis(inventory['chassis'])
        output_handler.print_inventory_servers(inventory['servers'])

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
