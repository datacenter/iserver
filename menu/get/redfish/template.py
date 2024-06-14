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
@click.option("--view", "-v", default=['identity'], help="[access|account|bios|cpu|endpoint|fan|gpu|hw|identity|mem|net|pci|power|psu|role|storage|thermal|all]", show_default=True, multiple=True)
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
        'access|account|bios|cpu|endpoint|fan|gpu|hw|identity|mem|net|pci|power|psu|role|storage|thermal|all',
        'identity',
        [
            'access:account,role',
            'hw:cpu,fan,gpu,mem,net,pci,psu,storage',
            'endpoint:endpoint'
        ]
    )
    if view is None:
        sys.exit(1)

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
            if properties_template_name in ['endpoint']:
                continue

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

        ctx.my_output.json_output(template_properties)

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

        if 'endpoint' in view:
            if redfish_settings is not None:
                ctx.my_output.default(
                    json.dumps(redfish_settings, indent=4)
                )

            return

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

        if 'bios' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'bios',
                    template_properties['bios'],
                    title=True
                )

        if 'cpu' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'cpu',
                    template_properties['cpu'],
                    title=True
                )

        if 'gpu' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'gpu',
                    template_properties['gpu'],
                    title=True
                )

        if 'mem' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'mem',
                    template_properties['mem'],
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

        if 'net' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'net',
                    template_properties['net'],
                    title=True
                )

        if 'pci' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'pci',
                    template_properties['pci'],
                    title=True
                )

        if 'fan' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'fan',
                    template_properties['fan'],
                    title=True
                )

        if 'psu' in view:
            if endpoint_type == 'ucsc':
                output_handler.print_ucsc_properties(
                    'psu',
                    template_properties['psu'],
                    title=True
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

        ctx.my_output.default('View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all', before_newline=True)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
