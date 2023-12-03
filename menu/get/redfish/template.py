import sys
import json
import threading
import traceback
import click

from lib.redfish import endpoint
from lib.redfish import endpoint_settings
from lib.redfish import output as redfish_output

from menu import common
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("template")
@click.pass_obj
@click.option("--type", "endpoint_type", type=click.Choice(['ucsc', 'fi', 'hpe', 'dell'], case_sensitive=False), default='ucsc', help="Redfish endpoint type")
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--inventory-type", default='', help="FI Inventory Type")
@click.option("--inventory-id", default='', help="FI Inventory Id")
@click.option("--cache", "cache_name", callback=validations.empty_string_to_none, default='', help="Cache name")
@click.option("--ttl", "cache_ttl", default=600, help="Cache TTL")
@click.option("--view", "-v", default=['identity'], help="[access|account|identity|power|role|storage|thermal|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_redfish_template_command(
        ctx,
        endpoint_type,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        inventory_type,
        inventory_id,
        cache_name,
        cache_ttl,
        view,
        output,
        devel
        ):
    """Get redfish template"""

    # iserver get redfish template

    ctx.developer = devel
    view = validations.validate_view(
        ctx,
        view,
        'access|account|identity|power|role|storage|thermal|all',
        'identity',
        [
            'access:account,role'
        ]
    )
    if view is None:
        sys.exit(1)

    try:
        common.flags_fixup(ctx, False, False, False)

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        handler_endpoint_type = endpoint_type

        if len(username) > 0:
            system_id = None

        if len(username) == 0 and cache_name is None:
            endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
                log_id=ctx.run_id
            )

            endpoint_id = endpoint_settings_handler.get_endpoint_id_with_ip(
                endpoint_ip
            )
            if endpoint_id is None:
                ctx.my_output.default('Endpoint not found in internal redfish database')
                raise ErrorExit

            redfish_settings = endpoint_settings_handler.get_redfish_endpoint_settings(endpoint_id)
            if redfish_settings is None:
                ctx.my_output.default('Selected server is not configured with Redfish access')
                raise ErrorExit

            if redfish_settings['endpoint']['type'] == 'generic':
                ctx.my_output.error(
                    'Endpoint properties template not supported on generic endpoint type'
                )
                raise ErrorExit

            endpoint_type = redfish_settings['endpoint']['type']
            endpoint_ip = redfish_settings['endpoint']['ip']
            endpoint_port = redfish_settings['endpoint']['port']
            username = redfish_settings['endpoint']['username']
            password = redfish_settings['endpoint']['password']
            inventory_type = redfish_settings['endpoint']['inventory_type']
            inventory_id = redfish_settings['endpoint']['inventory_id']
            system_id = endpoint_id

        if cache_name is not None:
            system_id = None
            handler_endpoint_type = 'cache'

        redfish_handler = endpoint.RedfishEndpoint(
            handler_endpoint_type,
            endpoint_ip,
            endpoint_port,
            username,
            password,
            system_id=system_id,
            cache_name=cache_name,
            get_timeout=120,
            auto_connect=False,
            ssl_verify=False,
            log_id=ctx.run_id
        )

        if endpoint_type == 'fi':
            redfish_handler.endpoint_handler.set_inventory(
                inventory_type,
                inventory_id
            )

        template_properties = {}
        for properties_template_name in view:
            if properties_template_name == 'inventory':
                if endpoint_type == 'fi':
                    template_properties[properties_template_name] = redfish_handler.endpoint_handler.get_inventory()

                continue

            template_properties[properties_template_name] = redfish_handler.endpoint_handler.get_template_properties(
                properties_template_name,
                cache_key=system_id,
                cache_ttl=cache_ttl
            )
            if template_properties[properties_template_name] is None:
                ctx.my_output.error(
                    'Failed to get template %s' % (properties_template_name)
                )
                raise ErrorExit

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(template_properties, indent=4)
            )
            return

        output_handler = redfish_output.RedfishOutput(log_id=ctx.run_id)

        if 'identity' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'identity',
                    template_properties['identity'],
                    title=True
                )

            if endpoint_type == 'hpe':
                output_handler.print_hpe_properties(
                    'identity',
                    template_properties['identity']
                )

            if endpoint_type == 'dell':
                output_handler.print_dell_properties(
                    'identity',
                    template_properties['identity']
                )

        if 'account' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'account',
                    template_properties['account'],
                    title=True
                )

        if 'role' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'role',
                    template_properties['role'],
                    title=True
                )

        if 'storage' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'storage',
                    template_properties['storage'],
                    title=True
                )

            if endpoint_type == 'hpe':
                output_handler.print_hpe_properties(
                    'storage',
                    template_properties['storage']
                )

            if endpoint_type == 'dell':
                output_handler.print_dell_properties(
                    'storage',
                    template_properties['storage']
                )

        if 'power' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'power',
                    template_properties['power']
                )

            if endpoint_type == 'hpe':
                output_handler.print_hpe_properties(
                    'power',
                    template_properties['power']
                )

            if endpoint_type == 'dell':
                output_handler.print_dell_properties(
                    'power',
                    template_properties['power']
                )

        if 'thermal' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'thermal',
                    template_properties['thermal'],
                    title=True
                )

            if endpoint_type == 'hpe':
                output_handler.print_hpe_properties(
                    'thermal',
                    template_properties['thermal']
                )

            if endpoint_type == 'dell':
                output_handler.print_dell_properties(
                    'thermal',
                    template_properties['thermal']
                )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
