import sys
import json
import threading
import traceback
import click

from lib.nexus import settings as nexus_settings
from lib.nexus import output as nexus_output
from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("mac")
@click.pass_obj
@click.option("--device", "device", default='', callback=validations.validate_nexus_any_name, help="Device name")
@click.option("--ip", "device_ip", default='', callback=validations.validate_ip, help="Device IP")
@click.option("--username", "device_username", default='', help="Device Username")
@click.option("--password", "device_password", default='', help="Device Password")
@click.option("--mac", default='', callback=validations.empty_string_to_none, help="Filter by mac address")
@click.option("--vlan", default='', callback=validations.empty_string_to_none, help="Filter by vlan")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--cache", "user_cache", type=click.Choice(['follow', 'on', 'off'], case_sensitive=False), default='follow', show_default=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nx_mac_command(
        ctx,
        device,
        device_ip,
        device_username,
        device_password,
        mac,
        vlan,
        view,
        user_cache,
        output,
        devel
        ):
    """Get mac address table mac"""

    # iserver get nx mac

    ctx.developer = devel
    ctx.output = output
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
        nexus_settings_handler = nexus_settings.NexusSettings(log_id=None)
        cache_enabled = nexus_settings_handler.is_nexus_cache_enabled()
        if user_cache == 'on':
            cache_enabled = True
        if user_cache == 'off':
            cache_enabled = False

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

        nexus_output_handler = nexus_output.NexusOutput(log_id=ctx.run_id)

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        object_filter = []
        if mac is not None:
            object_filter.append(
                'mac:%s' % (mac)
            )

        if vlan is not None:
            object_filter.append(
                'vlan:%s' % (vlan)
            )

        macs = []

        for device_handler in device_handlers:
            device_macs = device_handler['handler'].get_macs(
                object_filter=object_filter
            )
            if device_macs is not None:
                macs = macs + device_macs

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    macs,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(macs)

        if 'state' in view:
            nexus_output_handler.print_macs(
                macs,
                title=True
            )

        ctx.my_output.default('Filter: mac, vlan', before_newline=True)
        ctx.my_output.default('View:   state (def)')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
