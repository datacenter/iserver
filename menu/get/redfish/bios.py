import sys
import json
import threading
import traceback
import click

from lib import filter_helper
from lib.redfish import endpoint
from lib.redfish import output as redfish_output

from menu import common
from menu import progress
from menu import validations
from menu.get.redfish import validations as redfish_validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("bios")
@click.pass_obj
@click.option("--ip", "endpoint_ip", multiple=True, callback=validations.validate_ips, help="Management IP address")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--key", "key_filter", multiple=True, help="Key filter")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_redfish_bios_command(
        ctx,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        key_filter,
        view,
        output,
        devel
        ):
    """Get redfish bios"""

    # iserver get redfish bios

    ctx.developer = devel
    view = validations.validate_view(
        ctx,
        view,
        'state',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        common.flags_fixup(ctx, False, False, False)

        if len(endpoint_ip) == 0:
            endpoint_ip = redfish_validations.get_redfish_endpoint_ips(ctx)
            if endpoint_ip is None or len(endpoint_ip) == 0:
                raise ErrorExit

        endpoints = redfish_validations.get_redfish_endpoints(ctx, endpoint_ip, endpoint_port, username, password)
        if endpoints is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        bios_settings = {}

        for item in endpoints:
            redfish_handler = endpoint.RedfishEndpoint(
                item['type'],
                item['ip'],
                item['port'],
                item['username'],
                item['password'],
                system_id=item['system_id'],
                get_timeout=120,
                auto_connect=False,
                ssl_verify=False,
                log_id=ctx.run_id
            )

            endpoint_bios_settings = redfish_handler.endpoint_handler.get_template_properties(
                'bios',
            )
            if endpoint_bios_settings is None:
                ctx.my_output.error(
                    'Failed to get bios template %s' % (item['ip'])
                )
                raise ErrorExit

            filtered_bios_settings = {}
            for key in endpoint_bios_settings:
                if len(key_filter) == 0:
                    filtered_bios_settings[key] = endpoint_bios_settings[key]
                    continue

                matching = False
                for filtering_rule in key_filter:
                    if filter_helper.match_string(filtering_rule, key):
                        matching = True

                if matching:
                    filtered_bios_settings[key] = endpoint_bios_settings[key]
                    continue

            bios_settings[item['ip']] = filtered_bios_settings

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(bios_settings, indent=4)
            )
            return

        ctx.my_output.json_output(bios_settings)

        output_handler = redfish_output.RedfishOutput(log_id=ctx.run_id)

        output_handler.print_ucsc_properties(
            'bios-diff',
            bios_settings,
            title=True
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
