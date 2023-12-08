import sys
import json
import threading
import traceback
import click

from lib.aci import output as aci_output
from lib.psirt import main as psirt
from lib.psirt import output as psirt_output
from lib.psirt import settings

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
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_psirt_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        output,
        no_cache,
        devel
        ):
    """Get aci psirt"""

    # iserver get aci psirt

    ctx.developer = devel
    ctx.output = output

    try:
        settings_handler = settings.PsirtSettings(log_id=ctx.run_id)
        psirt_settings = settings_handler.get_psirt_settings()
        if psirt_settings is None:
            ctx.my_output.error('Failed to get psirt api settings')
            raise ErrorExit

        if not psirt_settings['enabled']:
            ctx.my_output.error('Psirt disabled')
            raise ErrorExit

        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handlers = validations.validate_apic_controllers(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            no_cache=no_cache
        )
        if apic_handlers is None:
            raise ErrorExit

        if len(apic_handlers) == 1:
            aci_output_handler.set_apic_off()

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        node_filter = []
        node_filter.append(
            'role:leaf'
        )

        advisories = {}
        apic_versions = {}

        for apic_handler in apic_handlers:
            apic_nodes = apic_handler['handler'].get_nodes(
                node_filter=node_filter
            )
            if apic_nodes is None:
                continue

            apic_version = None
            for node in apic_nodes:
                apic_version = node['version']
                if apic_version.startswith('n9000-'):
                    apic_version = apic_version[6:]
                break

            if apic_version is None:
                ctx.my_output.error(
                    'Failed to get APIC software version'
                )
                raise ErrorExit

            apic_versions[apic_handler['name']] = apic_version

            psirt_object_filter = []
            psirt_object_filter.append(
                'product:*aci*'
            )

            psirt_object_filter.append(
                'version:%s' % (apic_version)
            )

            psirt_handler = psirt.Psirt(psirt_settings['key'], psirt_settings['secret'], log_id=ctx.run_id)
            advisories[apic_handler['name']] = psirt_handler.get_advisories(
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
        for apic_name in advisories:
            ctx.my_output.default('Advisory - Apic: %s version %s' % (apic_name, apic_versions[apic_name]), underline=True, before_newline=True)
            psirt_output_handler.print_advisory_version(
                advisories[apic_name],
                title=False
            )

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
