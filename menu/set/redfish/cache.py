import sys
import threading
import traceback
import click

from lib.redfish import endpoint

from menu import common
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cache")
@click.pass_obj
@click.option("--name", "custom_cache_name", default='', help="Cache entry name")
@click.option("--type", "endpoint_type", type=click.Choice(['standard', 'ucsc', 'fi', 'dell', 'hpe'], case_sensitive=False), default='standard', help="Redfish endpoint type")
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Redfish management IP")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--ssl_verify", is_flag=True, default=False, help="SSL verify")
@click.option("--inventory-type", default='', help="FI Inventory Type")
@click.option("--inventory-id", default='', help="FI Inventory Id")
@click.option("--exclusions", is_flag=True, show_default=True, default=False, help="No uri exclusions in deep search")
@click.option("--max", "tree_max_execution_time", is_flag=False, type=click.INT, default=0, help="Max execution time in seconds")
@click.option("--timeout", "get_timeout", is_flag=False, show_default=True, default=120, type=click.INT, help="Get uri timeout")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_redfish_cache_command(
        ctx,
        custom_cache_name,
        endpoint_type,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        ssl_verify,
        inventory_type,
        inventory_id,
        exclusions,
        tree_max_execution_time,
        get_timeout,
        devel
        ):
    """Cache redfish endpoint resources"""

    # iserver set redfish cache

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        if endpoint_ip == '':
            ctx.my_output.error('Define endpoint IP address')
            raise ErrorExit

        if username == '':
            ctx.my_output.error('Define Redfish access username')
            raise ErrorExit

        if password == '':
            ctx.my_output.error('Define Redfish access password')
            raise ErrorExit

        if endpoint_type == 'fi':
            if inventory_type == '':
                ctx.my_output.error('Define FI inventory Type')
                raise ErrorExit

            if inventory_id == '':
                ctx.my_output.error('Define FI inentory ID')
                raise ErrorExit

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        redfish_handler = endpoint.RedfishEndpoint(
            endpoint_type,
            endpoint_ip,
            endpoint_port,
            username,
            password,
            get_timeout=get_timeout,
            ssl_verify=ssl_verify,
            deep_search_exlusions=exclusions,
            tree_max_execution_time=tree_max_execution_time,
            log_id=ctx.run_id,
            verbose=False,
            debug=False
        )

        if not redfish_handler.is_connected():
            ctx.busy = False
            ctx.my_output.error(
                'Redfish access failed'
            )
            raise ErrorExit

        # --type fi
        inventory = None
        if endpoint_type == 'fi':
            redfish_handler.endpoint_handler.set_inventory(
                inventory_type,
                inventory_id
            )

        endpoint_identity = redfish_handler.endpoint_handler.get_template_identity_properties()
        endpoint_identity['EndpointType'] = endpoint_type
        endpoint_identity['EndpointIp'] = endpoint_ip
        endpoint_identity['EndpointInventoryType'] = inventory_type
        endpoint_identity['EndpointInventoryId'] = inventory_id

        endpoint_resources = redfish_handler.get_tree(
            '/'
        )

        extra_resources = None
        if endpoint_type == 'fi':
            if inventory_type == 'Server':
                extra_resources = {}
                extra_resources['Chassis'] = redfish_handler.endpoint_handler.get_chassis()
                extra_resources['Servers'] = redfish_handler.endpoint_handler.get_servers()
                extra_resources['Inventory'] = redfish_handler.endpoint_handler.get_inventory()
                extra_resources['Power'] = redfish_handler.endpoint_handler.get_server_chassis_properties()

        ctx.busy = False

        cache_name = redfish_handler.set_redfish_cache_endpoint(
            endpoint_identity,
            endpoint_resources,
            extra_resources=extra_resources,
            custom_cache_name=custom_cache_name
        )

        if cache_name is None:
            ctx.my_output.error('Cache set failed')
            raise ErrorExit

        ctx.my_output.default(
            'Cache set successful: %s in file %s' % (
                cache_name,
                endpoint_identity['CacheFileName']
            )
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
