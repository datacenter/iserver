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


@click.command("vmedia-eject")
@click.pass_obj
@click.option("--type", "endpoint_type", type=click.Choice(['standard', 'ucsc', 'fi', 'bmc', 'dell', 'hpe'], case_sensitive=False), default='standard', help="Redfish endpoint type")
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--inventory-type", default='', help="FI Inventory Type")
@click.option("--inventory-id", default='', help="FI Inventory Id")
@click.option("--id", "vmedia_id", type=click.INT, default=-1, help="Virtual media id")
def set_redfish_vmedia_eject_command(
        ctx,
        endpoint_type,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        inventory_type,
        inventory_id,
        vmedia_id
        ):
    """Insert virtual media (http)"""

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

        if vmedia_id < 0:
            user_input = input('Virtual media id: ')
            try:
                vmedia_id = int(user_input)
            except BaseException:
                vmedia_id = -1

            if vmedia_id < 0:
                raise ErrorExit
                    
        redfish_handler = redfish_common.get_redfish_handler(ctx, params)
        if redfish_handler is None:
            raise ErrorExit

        success = redfish_handler.endpoint_handler.eject_media(
            virtual_media_id=vmedia_id
        )
        if not success:
            ctx.my_output.error('Media eject failed...')
            raise ErrorExit

        ctx.my_output.default('Virtual media ejected')
        
        response = redfish_handler.endpoint_handler.get_virtual_media(virtual_media_id=vmedia_id)
        if response is None:
            ctx.my_output.error('Failed to get virtual media')
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
