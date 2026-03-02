import sys
import json
import threading
import traceback
import click

from menu.get.redfish import common as redfish_common
from menu import common
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("boot-override")
@click.pass_obj
@click.option("--type", "endpoint_type", type=click.Choice(['standard', 'ucsc', 'fi', 'bmc', 'dell', 'hpe'], case_sensitive=False), default='standard', help="Redfish endpoint type")
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--inventory-type", default='', help="FI Inventory Type")
@click.option("--inventory-id", default='', help="FI Inventory Id")
@click.option("--timeout", "get_timeout", is_flag=False, show_default=True, default=10, type=click.INT, help="Get uri timeout")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def get_redfish_boot_override_command(
        ctx,
        endpoint_type,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        inventory_type,
        inventory_id,
        get_timeout,
        output
        ):
    """Get boot properties"""

    ctx.developer = False

    try:
        common.flags_fixup(ctx, False, False, False)

        params = {}
        params['endpoint_type'] = endpoint_type
        params['endpoint_ip'] = endpoint_ip
        params['endpoint_port'] = endpoint_port
        params['username'] = username
        params['password'] = password
        params['inventory_type'] = inventory_type
        params['inventory_id'] = inventory_id

        params = redfish_common.input_params(ctx, params)
        if params is None:
            raise ErrorExit
        
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        redfish_handler = redfish_common.get_redfish_handler(ctx, params, get_timeout=get_timeout)
        if redfish_handler is None:
            raise ErrorExit
        
        response = redfish_handler.endpoint_handler.get_boot_properties()

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(response, indent=4)
            )

        if output == 'default':
            if response is None:
                ctx.my_output.error('Failed to get boot properties')
                raise ErrorExit
            
            ctx.my_output.default(
                json.dumps(response, indent=4),
                wrap='~~~',
                before_newline=True
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
