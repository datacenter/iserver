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


@click.command("pc")
@click.pass_obj
@click.option("--device", "device", default='', callback=validations.validate_nexus_any_name, help="Device name")
@click.option("--ip", "device_ip", default='', callback=validations.validate_ip, help="Device IP")
@click.option("--username", "device_username", default='', help="Device Username")
@click.option("--password", "device_password", default='', help="Device Password")
@click.option("--view", "-v", default=['state'], help="[db,lb,state,traffic,all]", show_default=True, multiple=True)
@click.option("--cache", "user_cache", type=click.Choice(['follow', 'on', 'off'], case_sensitive=False), default='follow', show_default=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nx_pc_command(
        ctx,
        device,
        device_ip,
        device_username,
        device_password,
        view,
        user_cache,
        output,
        devel
        ):
    """Get pc"""

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'db|lb|state|traffic|all',
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

        if output == 'default':
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        pcs = {}
        pcs['db'] = []
        pcs['lb'] = []
        pcs['state'] = []
        pcs['traffic'] = []

        for device_handler in device_handlers:
            if 'db' in view:
                device_db = device_handler['handler'].get_pc_database()
                if device_db is not None:
                    pcs['db'].append(
                        device_db
                    )

            if 'lb' in view:
                device_lb = device_handler['handler'].get_pc_lb()
                if device_lb is not None:
                    pcs['lb'].append(
                        device_lb
                    )

            if 'state' in view:
                device_state = device_handler['handler'].get_pc_state()
                if device_state is not None:
                    pcs['state'] = pcs['state'] + device_state

            if 'traffic' in view:
                device_traffic = device_handler['handler'].get_pc_traffic()
                if device_traffic is not None:
                    pcs['traffic'] = pcs['traffic'] + device_traffic

        ctx.busy = False

        ctx.my_output.json_output(pcs)

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    pcs,
                    indent=4
                )
            )
            return

        if 'state' in view:
            nexus_output_handler.print_pc_state(
                pcs['state'],
                title=True
            )

        if 'db' in view:
            nexus_output_handler.print_pc_database(
                pcs['db'],
                title=True
            )

        if 'lb' in view:
            nexus_output_handler.print_pc_lb(
                pcs['lb'],
                title=True
            )

        if 'traffic' in view:
            nexus_output_handler.print_pc_traffic(
                pcs['traffic'],
                title=True
            )

        ctx.my_output.default('Filter: --', before_newline=True)
        ctx.my_output.default('View:   db, lb, state (def), traffic, all')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
