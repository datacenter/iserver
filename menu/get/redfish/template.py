import sys
import json
import threading
import traceback
import click

from menu.get.redfish import common as redfish_common
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
@click.option("--type", "endpoint_type", type=click.Choice(['ucsc', 'fi', 'bmc', 'hpe', 'dell'], case_sensitive=False), default='ucsc', help="Redfish endpoint type")
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--inventory-type", default='', help="FI Inventory Type")
@click.option("--inventory-id", default='', help="FI Inventory Id")
@click.option("--timeout", "get_timeout", is_flag=False, show_default=True, default=10, type=click.INT, help="Get uri timeout")
@click.option("--view", "-v", default=['identity'], help="[access|account|bios|cpu|endpoint|fan|gpu|hw|identity|mem|net|pci|power|psu|role|storage|thermal|all]", show_default=True, multiple=True)
@click.option("--no-cache", is_flag=True, show_default=True, default=False, help="Disable endpoint cache")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def get_redfish_template_command(
        ctx,
        endpoint_type,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        inventory_type,
        inventory_id,
        get_timeout,
        view,
        no_cache,
        output
        ):
    """Get redfish template"""

    # iserver get redfish template

    ctx.developer = False
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

        params = {}
        params['endpoint_type'] = endpoint_type
        params['endpoint_ip'] = endpoint_ip
        params['endpoint_port'] = endpoint_port
        params['username'] = username
        params['password'] = password
        params['inventory_type'] = inventory_type
        params['inventory_id'] = inventory_id

        params = redfish_common.input_params(ctx, params, cache_enabled=not no_cache)
        if params is None:
            raise ErrorExit

        redfish_handler = redfish_common.get_redfish_handler(ctx, params, get_timeout=get_timeout)
        if redfish_handler is None:
            raise ErrorExit

        template_properties = {}
        for properties_template_name in view:
            if properties_template_name in ['endpoint']:
                continue

            if properties_template_name == 'inventory':
                if endpoint_type == 'fi':
                    template_properties[properties_template_name] = redfish_handler.endpoint_handler.get_inventory()

                continue

            template_properties[properties_template_name] = redfish_handler.endpoint_handler.get_template_properties(
                properties_template_name
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
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'identity',
                    template_properties['identity']
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
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'account',
                    template_properties['account']
                )

        if 'role' in view:
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'role',
                    template_properties['role']
                )

        if 'bios' in view:
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'bios',
                    template_properties['bios']
                )

        if 'cpu' in view:
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'cpu',
                    template_properties['cpu']
                )

        if 'gpu' in view:
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'gpu',
                    template_properties['gpu']
                )

        if 'mem' in view:
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'mem',
                    template_properties['mem']
                )

        if 'storage' in view:
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'storage',
                    template_properties['storage']
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
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'net',
                    template_properties['net']
                )

        if 'pci' in view:
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'pci',
                    template_properties['pci']
                )

        if 'fan' in view:
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'fan',
                    template_properties['fan']
                )

        if 'psu' in view:
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'psu',
                    template_properties['psu']
                )

        if 'power' in view:
            if endpoint_type in ['ucsc', 'fi']:
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
            if endpoint_type in ['ucsc', 'fi']:
                output_handler.print_ucsc_properties(
                    'thermal',
                    template_properties['thermal']
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
