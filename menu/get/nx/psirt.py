import sys
import json
import threading
import traceback
import click

from lib.aci import output as aci_output
from lib.psirt import main as psirt
from lib.psirt import output as psirt_output
from lib.psirt import settings
from lib.nexus import settings as nexus_settings

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("psirt")
@click.pass_obj
@click.option("--device", "device", default='', callback=validations.validate_nexus_any_name, help="Device name")
@click.option("--ip", "device_ip", default='', callback=validations.validate_ip, help="Device IP")
@click.option("--username", "device_username", default='', help="Device Username")
@click.option("--password", "device_password", default='', help="Device Password")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nx_psirt_command(
        ctx,
        device,
        device_ip,
        device_username,
        device_password,
        view,
        output,
        devel
        ):
    """Get nx psirt"""

    # iserver get nx psirt

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
        settings_handler = settings.PsirtSettings(log_id=ctx.run_id)
        psirt_settings = settings_handler.get_psirt_settings()
        if psirt_settings is None:
            ctx.my_output.error('Failed to get psirt api settings')
            raise ErrorExit

        if not psirt_settings['enabled']:
            ctx.my_output.error('Psirt disabled')
            raise ErrorExit

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

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        advisories = {}
        node_versions = {}

        for device_handler in device_handlers:
            device_versions = device_handler['handler'].get_versions()

            if len(device_versions) != 1:
                continue

            device_version = device_versions[0]['nxos_ver_str']
            node_versions[device_handler['name']] = device_version

            psirt_object_filter = []
            psirt_object_filter.append(
                'product:*nx-os*'
            )

            psirt_object_filter.append(
                'version:%s' % (device_version)
            )

            psirt_handler = psirt.Psirt(psirt_settings['key'], psirt_settings['secret'], log_id=ctx.run_id)
            advisories[device_handler['name']] = psirt_handler.get_advisories(
                psirt_object_filter
            )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    advisories,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(advisories)

        psirt_output_handler = psirt_output.PsirtOutput(log_id=ctx.run_id)
        for device_name in advisories:
            ctx.my_output.default('Advisory - Apic: %s version %s' % (device_name, node_versions[device_name]), underline=True, before_newline=True)
            psirt_output_handler.print_advisory_version(
                advisories[device_name],
                title=False
            )

        ctx.my_output.default('Filter: --', before_newline=True)
        ctx.my_output.default('View:   state (def)')

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
