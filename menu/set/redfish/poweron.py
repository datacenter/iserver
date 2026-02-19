import sys
import traceback
import click

from menu.get.redfish import common as redfish_common
from menu import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("power-on")
@click.pass_obj
@click.option("--type", "endpoint_type", type=click.Choice(['standard', 'ucsc', 'fi', 'dell', 'hpe'], case_sensitive=False), default='standard', help="Redfish endpoint type")
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--inventory-type", default='', help="FI Inventory Type")
@click.option("--inventory-id", default='', help="FI Inventory Id")
@click.option("--timeout", "get_timeout", is_flag=False, show_default=True, default=10, type=click.INT, help="Get uri timeout")
def set_redfish_power_on_command(
        ctx,
        endpoint_type,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        inventory_type,
        inventory_id,
        get_timeout
        ):
    """Power on"""

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
        
        redfish_handler = redfish_common.get_redfish_handler(ctx, params, get_timeout=get_timeout)
        if redfish_handler is None:
            raise ErrorExit

        success = redfish_handler.endpoint_handler.power_on()
        if not success:
            ctx.my_output.error('Server power on failed...')
            raise ErrorExit

        ctx.my_output.default('Power on requested via Redfish API')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
