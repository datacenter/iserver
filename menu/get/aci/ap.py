import sys
import json
import threading
import traceback
import click

from lib.aci import output as aci_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ap")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "ap_name", default='', callback=validations.validate_apic_tenant_name, help="Filter by application profile name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--epg", "epg_name", default='', callback=validations.empty_string_to_none, help="Filter by epg name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_ap_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        ap_name,
        tenant_name,
        epg_name,
        output,
        devel
        ):
    """Get aci application profile"""

    # iserver get aci ap

    ctx.developer = devel
    if output == 'json':
        ctx.output = 'json'
    else:
        ctx.output = 'default'

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_username,
            controller_password
        )
        if apic_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        application_profile_filter = []

        tenant_filtered = False
        if ap_name is not None:
            application_profile_filter.append(
                'name:%s' % (ap_name['name'])
            )

            if ap_name['tenant'] is not None:
                tenant_filtered = True
                application_profile_filter.append(
                    'tenant:%s' % (ap_name['tenant'])
                )

        if tenant_name is not None:
            if tenant_filtered:
                ctx.my_output.error(
                    'Define tenant in one place'
                )
                raise ErrorExit

            application_profile_filter.append(
                'tenant:%s' % (tenant_name)
            )

        if epg_name is not None:
            application_profile_filter.append(
                'epg:%s' % (epg_name)
            )

        application_profiles = apic_handler.get_application_profiles(
            application_profile_filter=application_profile_filter
        )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    application_profiles,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(application_profiles)

        aci_output_handler.print_application_profiles(
            application_profiles
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
