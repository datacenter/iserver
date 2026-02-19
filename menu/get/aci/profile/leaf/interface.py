import sys
import json
import threading
import traceback
import click

from menu import validations
from menu import progress

from lib.aci import output as aci_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("interface")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "profile_name", default='', callback=validations.empty_string_to_none, help="Filter by profile name")
@click.option("--view", "-v", default=['state'], help="[state|usage]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--ttl", "requested_ttl", default=-1, show_default=True, help="Cache ttl")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_profile_leaf_interface_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        profile_name,
        view,
        output,
        requested_ttl,
        devel
        ):
    """Get aci leaf interface profiles"""

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|usage',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            requested_ttl=requested_ttl
        )
        if apic_handler is None:
            raise ErrorExit

        profile_filter = []
        if profile_name is not None:
            profile_filter.append(
                'name:%s' % (profile_name)
            )

        usage_info=False
        if 'usage' in view:
            usage_info=True

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        profiles = apic_handler.get_profiles_leaf_interface(
            profile_filter=profile_filter,
            node_interface_info=usage_info,
            reln_info=True
        )

        ctx.busy = False

        if profiles is None:
            ctx.my_output.error('Failed to get information')
            raise NoResultExit

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    profiles,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(profiles)

        if 'state' in view:
            aci_output_handler.print_profiles_leaf_interface(
                profiles,
                title=True
            )

        if 'usage' in view:
            aci_output_handler.print_profiles_leaf_interface_usage(
                profiles,
                title=True
            )

        if len(profiles) == 0:
            raise NoResultExit

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
