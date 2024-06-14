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


@click.command("uri")
@click.pass_obj
@click.option("--type", "endpoint_type", type=click.Choice(['standard', 'ucsc', 'fi', 'dell', 'hpe'], case_sensitive=False), default='standard', help="Redfish endpoint type")
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--inventory-type", default='', help="FI Inventory Type")
@click.option("--inventory-id", default='', help="FI Inventory Id")
@click.option("--uri", "redfish_path", default='/', callback=validations.validate_redfish_path, help="Redfish resource uri")
@click.option("--property", "redfish_properties", multiple=True, help="Select redfish properties within resource")
@click.option("--key", "key_filter", multiple=True, help="Filter keys")
@click.option("--value", "value_filter", multiple=True, help="Filter values")
@click.option("--description", is_flag=True, show_default=True, default=False, help="Description properties only")
@click.option("--children", is_flag=True, show_default=True, default=False, help="Children only")
@click.option("--oem", is_flag=True, show_default=True, default=False, help="Oem only")
@click.option("--action", is_flag=True, show_default=True, default=False, help="Action only")
@click.option("--deep", is_flag=True, show_default=True, default=False, help="Recursive iteration")
@click.option("--no-exclusions", is_flag=True, show_default=True, default=False, help="No uri exclusions in deep search")
@click.option("--max", "tree_max_execution_time", is_flag=False, type=click.INT, default=120, help="Max execution time in seconds")
@click.option("--timeout", "get_timeout", is_flag=False, show_default=True, default=10, type=click.INT, help="Get uri timeout")
@click.option("--cache", "cache_name", callback=validations.empty_string_to_none, default='', help="Cache name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_redfish_uri_command(
        ctx,
        endpoint_type,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        inventory_type,
        inventory_id,
        redfish_path,
        redfish_properties,
        key_filter,
        value_filter,
        description,
        children,
        oem,
        action,
        deep,
        no_exclusions,
        tree_max_execution_time,
        get_timeout,
        cache_name,
        output,
        devel
        ):
    """Get redfish uri resources"""

    # iserver get redfish uri

    ctx.developer = devel

    try:
        common.flags_fixup(ctx, False, False, False)

        if cache_name is None:
            if len(endpoint_ip) == 0:
                endpoint_ip = input('Redfish endpoint IP address: ')
                if not ip_helper.is_valid_ipv4_address(endpoint_ip):
                    ctx.my_output.error('IPv4 address invalid')
                    raise ErrorExit

            endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
                log_id=ctx.run_id
            )

            endpoint_id = endpoint_settings_handler.get_endpoint_id_with_ip(
                endpoint_ip
            )
            if endpoint_id is None:
                ctx.my_output.default('Endpoint not found in internal redfish database. Provide full access details.')
                system_id = None

                endpoint_port = input('Redfish endpoint port [def. 443]: ')
                if len(endpoint_port) == 0:
                    endpoint_port = 443
                else:
                    try:
                        endpoint_port = int(endpoint_port)
                    except BaseException:
                        ctx.my_output.error('Port (int) value expected')
                        endpoint_port = None

                if endpoint_port is None:
                    raise ErrorExit

                username = input('Redfish authentication username: ')
                if len(username) == 0:
                    raise ErrorExit

                password = input('Redfish authentication password: ')
                if len(password) == 0:
                    raise ErrorExit

                handler_endpoint_type = input('Endpoint type [ucsc, fi, dell, hp]: ')
                if len(handler_endpoint_type) == 0 or handler_endpoint_type not in ['ucsc', 'fi', 'dell', 'hp']:
                    raise ErrorExit

                if handler_endpoint_type == 'fi':
                    inventory_type = input('Inventory type: ')
                    if len(inventory_type) == 0:
                        raise ErrorExit

                    inventory_id = input('Inventory id: ')
                    if len(inventory_id) == 0:
                        raise ErrorExit

                redfish_settings = None
            else:
                redfish_settings = endpoint_settings_handler.get_redfish_endpoint_settings(endpoint_id)
                if redfish_settings is None:
                    ctx.my_output.default('Selected server in internal redfish database and is not configured with Redfish access')
                    raise ErrorExit

                ctx.my_output.default('Endpoint found in internal redfish database.')

                if redfish_settings['endpoint']['type'] == 'generic':
                    ctx.my_output.error(
                        'Endpoint properties template not supported on generic endpoint type'
                    )
                    raise ErrorExit

                system_id = endpoint_id
                handler_endpoint_type = redfish_settings['endpoint']['type']
                endpoint_ip = redfish_settings['endpoint']['ip']
                endpoint_port = redfish_settings['endpoint']['port']

                update_requested = False
                if len(username) == 0:
                    username = redfish_settings['endpoint']['username']
                else:
                    update_requested = True
                if len(password) == 0:
                    password = redfish_settings['endpoint']['password']
                else:
                    update_requested = True
                if len(inventory_type) == 0:
                    inventory_type = redfish_settings['endpoint']['inventory_type']
                else:
                    update_requested = True
                if len(inventory_id) == 0:
                    inventory_id = redfish_settings['endpoint']['inventory_id']
                else:
                    update_requested = True


                if update_requested:
                    ctx.my_output.default('Update redfish endpoint settings?')
                    if common.get_confirmation():
                        redfish_endpoint_settings = {}
                        redfish_endpoint_settings['type'] = handler_endpoint_type
                        redfish_endpoint_settings['ip'] = endpoint_ip
                        redfish_endpoint_settings['port'] = endpoint_port
                        redfish_endpoint_settings['username'] = username
                        redfish_endpoint_settings['password'] = password
                        redfish_endpoint_settings['inventory_type'] = inventory_type
                        redfish_endpoint_settings['inventory_id'] = inventory_id

                        success = endpoint_settings_handler.set_redfish_endpoint_access(
                            redfish_endpoint_settings,
                            endpoint_id
                        )
                        if success:
                            ctx.my_output.default('Updated')
                            redfish_settings = endpoint_settings_handler.get_redfish_endpoint_settings(endpoint_id)
                            if redfish_settings is None:
                                ctx.my_output.default('Something went wrong after update...')
                                raise ErrorExit
                        else:
                            ctx.my_output.error('Update failed')

        if cache_name is not None:
            system_id = None
            handler_endpoint_type = 'cache'

        ctx.my_output.default('Requested URI: %s' % (redfish_path))

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        redfish_handler = endpoint.RedfishEndpoint(
            handler_endpoint_type,
            endpoint_ip,
            endpoint_port,
            username,
            password,
            system_id=system_id,
            cache_name=cache_name,
            get_timeout=get_timeout,
            auto_connect=True,
            ssl_verify=False,
            deep_search_exlusions=not no_exclusions,
            tree_max_execution_time=tree_max_execution_time,
            log_id=ctx.run_id
        )

        if endpoint_type == 'fi':
            redfish_handler.endpoint_handler.set_inventory(
                inventory_type,
                inventory_id
            )

        if not redfish_handler.is_connected():
            ctx.busy = False
            ctx.my_output.error(
                'Redfish access failed'
            )
            raise ErrorExit

        output_handler = redfish_output.RedfishOutput(log_id=ctx.run_id)

        # --children option handler with optional --deep
        if children:
            children_paths = redfish_handler.get_children(
                redfish_path,
                deep
            )

            ctx.busy = False

            if children is None:
                ctx.my_output.error(
                    'Children collection failed: %s' % (redfish_path)
                )
                raise ErrorExit

            output_handler.print_children(
                redfish_handler.endpoint_handler.path_fixup(redfish_path),
                children_paths,
                deep,
                output
            )

            return

        # --description option handler with optional --deep
        if description:
            description_tree = redfish_handler.get_descriptions(
                redfish_path,
                deep
            )

            ctx.busy = False

            if description_tree is None:
                ctx.my_output.error(
                    'Description collection failed: %s' % (redfish_path)
                )
                raise ErrorExit

            output_handler.print_tree(
                description_tree,
                output
            )

            return

        # --action option handler with optional --deep
        if action:
            action_tree = redfish_handler.get_action(
                redfish_path,
                deep
            )

            ctx.busy = False

            if action_tree is None:
                ctx.my_output.error(
                    'Action collection failed: %s' % (redfish_path)
                )
                raise ErrorExit

            output_handler.print_tree(
                action_tree,
                output
            )

            return

        # --oem option handler with optional --deep
        if oem:
            oem_tree = redfish_handler.get_oem(
                redfish_path,
                deep
            )

            ctx.busy = False

            if oem_tree is None:
                ctx.my_output.error(
                    'Oem collection failed: %s' % (redfish_path)
                )
                raise ErrorExit

            output_handler.print_tree(
                oem_tree,
                output
            )

            return

        # --key option handler with optional --deep
        if len(key_filter) > 0:
            key_tree = redfish_handler.get_keys(
                redfish_path,
                deep,
                key_filter
            )

            ctx.busy = False

            if key_tree is None:
                ctx.my_output.error(
                    'Oem collection failed: %s' % (redfish_path)
                )
                raise ErrorExit

            output_handler.print_tree(
                key_tree,
                output
            )

            return

        # --value option handler with optional --deep
        if len(value_filter) > 0:
            key_tree = redfish_handler.get_values(
                redfish_path,
                deep,
                value_filter
            )

            ctx.busy = False

            if key_tree is None:
                ctx.my_output.error(
                    'Value collection failed: %s' % (redfish_path)
                )
                raise ErrorExit

            output_handler.print_tree(
                key_tree,
                output
            )

            return

        # --path with deep
        if deep:
            tree = redfish_handler.get_tree(
                redfish_path
            )

            ctx.busy = False

            if output == 'json':
                ctx.my_output.default(
                    json.dumps(tree, indent=4)
                )

            if output == 'default':
                ctx.my_output.default('')
                for uri in tree:
                    if tree[uri] is not None:
                        ctx.my_output.default(uri, underline=True)
                        ctx.my_output.default(json.dumps(tree[uri], indent=4))
                        ctx.my_output.default('')

            return

        # --path and optional property selection
        properties = redfish_handler.get_properties(
            redfish_path,
            redfish_properties
        )
        if properties is None:
            ctx.busy = False
            ctx.my_output.error(
                'Redfish call failed: %s' % (redfish_path)
            )
            raise ErrorExit

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(properties, indent=4)
            )

        if output == 'default':
            ctx.my_output.default('')
            ctx.my_output.default(
                redfish_handler.endpoint_handler.path_fixup(
                    redfish_path
                ),
                underline=True
            )
            ctx.my_output.default(
                json.dumps(properties, indent=4)
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
