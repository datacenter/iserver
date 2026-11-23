import sys
import json
import threading
import traceback
import click

from lib.intersight import compute
from lib.intersight import compute_output
from lib.nexus import settings as nexus_settings

from menu import defaults
from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("server")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--device", "device", default='', callback=validations.validate_nexus_any_name, help="Device name")
@click.option("--ip", "device_ip", default='', callback=validations.validate_ip, help="Device IP")
@click.option("--username", "device_username", default='', help="Device Username")
@click.option("--password", "device_password", default='', help="Device Password")
@click.option("--address", "server_ip", callback=validations.validate_ip, help="Server IP")
@click.option("--view", "-v", default=['all'], help="[lacp|lldp|mac|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nx_server_command(
        ctx,
        iaccount,
        device,
        device_ip,
        device_username,
        device_password,
        server_ip,
        view,
        output,
        devel
        ):
    """Get server information"""

    # iserver get nx xd server

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'lacp|lldp|mac|all',
        'all',
        []
    )

    try:
        nexus_settings_handler = nexus_settings.NexusSettings(log_id=None)
        cache_enabled = nexus_settings_handler.is_nexus_cache_enabled()

        device_handlers = validations.validate_nexus_devices(
            ctx,
            device,
            device_ip,
            device_username,
            device_password,
            cache_enabled=cache_enabled
        )
        if device_handlers is None:
            raise ErrorExit

        if output != 'json':
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        compute_output_handler = compute_output.ComputeOutput(log_id=ctx.run_id)
        compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
        match_rules = compute_handler.get_mo_match_rules(
            ip_filter=[server_ip]
        )
        servers_mo = compute_handler.get_mo(
            match_rules=match_rules,
            include_rack=True,
            include_blade=True
        )
        if len(servers_mo) == 0:
            ctx.busy = False
            ctx.my_output.error('Server not found')
            raise ErrorExit

        if len(servers_mo) > 1:
            ctx.busy = False
            ctx.my_output.error('Multiple servers found')
            raise ErrorExit

        settings = {}
        settings['net'] = True

        servers_info = compute_handler.get_info(
            servers_mo,
            settings,
            None,
            0
        )
        server_info = servers_info[0]
        for device_handler in device_handlers:
            server_info = device_handler['handler'].get_server_connectivity(
                server_info
            )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    server_info['MacAddressInfo'],
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(server_info['MacAddressInfo'])

        compute_output_handler.print_summary_table(
            [server_info],
            title=True
        )

        compute_output_handler.print_nx(
            server_info,
            title=True
        )

        ctx.my_output.default('Filter: --', before_newline=True)
        ctx.my_output.default('View:   lacp, lldp, mac, all (def)')

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
