import sys
import json
import traceback
import click

from menu.get.redfish import common as redfish_common
from menu import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("boot-override")
@click.pass_obj
@click.option("--type", "endpoint_type", type=click.Choice(['standard', 'ucsc', 'fi', 'dell', 'hpe'], case_sensitive=False), default='standard', help="Redfish endpoint type")
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--inventory-type", default='', help="FI Inventory Type")
@click.option("--inventory-id", default='', help="FI Inventory Id")
@click.option("--target", type=click.Choice(['None', 'Pxe', 'Floppy', 'Cd', 'Hdd', 'BiosSetup', 'Diags'], case_sensitive=True), help="Boot target")
@click.option("--enabled", type=click.Choice(['Once', 'Continuous', 'Disabled'], case_sensitive=True), default='Once', help="Boot target")
@click.option("--timeout", "get_timeout", is_flag=False, show_default=True, default=10, type=click.INT, help="Get uri timeout")
def set_redfish_boot_override_command(
        ctx,
        endpoint_type,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        inventory_type,
        inventory_id,
        target,
        enabled,
        get_timeout
        ):
    """Set redfish boot override property"""

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
        
        if target is None:
            target = input('Boot target [None, Pxe, Floppy, Cd, Hdd, BiosSetup, Diags]: ')
            if len(target) == 0 or target not in ['None', 'Pxe', 'Floppy', 'Cd', 'Hdd', 'BiosSetup', 'Diags']:
                raise ErrorExit
        
        if target == None:
            enabled = 'Disabled'

        if enabled is None:
            enabled = input('Enabled [Once, Continuous, Disabled]: ')
            if len(enabled) == 0 or enabled not in ['Once', 'Continuous', 'Disabled']:
                raise ErrorExit
            
        redfish_handler = redfish_common.get_redfish_handler(ctx, params, get_timeout=get_timeout)
        if redfish_handler is None:
            raise ErrorExit

        response = redfish_handler.endpoint_handler.get_boot_properties()
        if response is None:
            ctx.my_output.error('Failed to get boot properties before one time boot source change')
            raise ErrorExit
        
        ctx.my_output.default(
            json.dumps(response, indent=4)
        )
        
        ctx.my_output.default('Set one time boot source: %s enabled %s' % (target, enabled), before_newline=True, after_newline=True)
        success = redfish_handler.endpoint_handler.set_one_time_boot_source(
            target,
            enabled=enabled
        )
        if not success:
            ctx.my_output.error('Redfish API failed')
            raise ErrorExit

        if not redfish_handler.reconnect():
            ctx.busy = False
            ctx.my_output.error(
                'Redfish reconnect failed'
            )
            raise ErrorExit
                
        response = redfish_handler.endpoint_handler.get_boot_properties()
        if response is None:
            ctx.my_output.error('Failed to get boot properties after one time boot source change')
            raise ErrorExit
        
        ctx.my_output.default(
            json.dumps(response, indent=4)
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
