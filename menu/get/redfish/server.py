import sys
import json
import threading
import traceback
import click

from lib.redfish import endpoint
from lib.redfish import endpoint_settings

from menu import common
from menu import defaults
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("server")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_filter_ip, help="Management IP address or subnet filter")
@click.option("--name", "name_filter", default='', help="Name loose match filter")
@click.option("--serial", "serial_filter", default='', callback=validations.validate_filter_serials, help="Serial strict match filter")
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
@click.option("--template", "properties_template_name", is_flag=False, show_default=False, default='', help="Endpoint properties template")
@click.option("--timeout", "get_timeout", is_flag=False, show_default=True, default=10, type=click.INT, help="Get uri timeout")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_redfish_server_command(
        ctx,
        iaccount,
        ip_filter,
        name_filter,
        serial_filter,
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
        properties_template_name,
        get_timeout,
        output,
        verbose,
        devel
        ):
    """Get redfish uri resources - indirect mode"""

    # iserver get redfish ucsc

    ctx.developer = devel

    silent = False
    debug = False

    if output == 'json':
        verbose = False
        ctx.log_prompt = False
    else:
        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

    common.flags_fixup(ctx, silent, verbose, debug)

    try:
        if len(properties_template_name) > 0:
            get_timeout = 120

        group_serials = []
        servers = common.get_selected_servers(
            ctx,
            iaccount,
            group_serials,
            serial_filter,
            name_filter,
            ip_filter,
            confirm=False,
            workflow=None,
            locator=False,
            registration=False,
            server_setting_id=False,
            show_servers=False,
            allow_all=False
        )
        if servers is None or len(servers) == 0:
            ctx.my_output.default('No servers found')
            raise ErrorExit

        if len(servers) > 1:
            ctx.my_output.default('Select single server')
            raise ErrorExit

        endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
            log_id=ctx.run_id
        )
        redfish_settings = endpoint_settings_handler.get_redfish_endpoint_settings(servers[0]['Serial'])
        if redfish_settings is None:
            ctx.my_output.default('Select server is not configured with Redfish access')
            raise ErrorExit

        redfish_handler = endpoint.RedfishEndpoint(
            redfish_settings['endpoint']['type'],
            redfish_settings['endpoint']['ip'],
            redfish_settings['endpoint']['port'],
            redfish_settings['endpoint']['username'],
            redfish_settings['endpoint']['password'],
            get_timeout=get_timeout,
            ssl_verify=False,
            deep_search_exlusions=not no_exclusions,
            tree_max_execution_time=tree_max_execution_time,
            log_id=ctx.run_id,
            verbose=verbose,
            debug=debug
        )

        if redfish_settings['endpoint']['type'] == 'fi':
            redfish_handler.endpoint_handler.set_inventory(
                redfish_settings['endpoint']['inventory_type'],
                redfish_settings['endpoint']['inventory_id']
            )

        if len(properties_template_name) > 0 and redfish_settings['endpoint']['type'] == 'generic':
            ctx.busy = False
            ctx.my_output.error(
                'Endpoint properties template not supported on generic endpoint type'
            )
            raise ErrorExit

        if not redfish_handler.is_connected():
            ctx.busy = False
            ctx.my_output.error(
                'Redfish access failed'
            )
            raise ErrorExit

        # --template option
        if len(properties_template_name) > 0:
            properties = redfish_handler.endpoint_handler.get_template_properties(
                properties_template_name
            )
            if properties is None:
                ctx.busy = False
                raise ErrorExit

            ctx.busy = False

            if output == 'json':
                ctx.my_output.default(
                    json.dumps(properties, indent=4)
                )

            if output == 'default':
                redfish_handler.endpoint_handler.print_template_properties(
                    properties_template_name,
                    properties
                )

            return

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

            redfish_handler.print_children(
                redfish_path,
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

            redfish_handler.print_tree(
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

            redfish_handler.print_tree(
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

            redfish_handler.print_tree(
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

            redfish_handler.print_tree(
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

            redfish_handler.print_tree(
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
