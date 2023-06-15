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


class NoResultExit(Exception):
    pass


@click.command("port")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--aaep", default='', callback=validations.empty_string_to_none, help="Filter by aaep")
@click.option("--view", "-v", type=click.Choice(['default', 'aaep'], case_sensitive=False), multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_pg_access_interface_port_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        name,
        aaep,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci policy group interface port"""

    # iserver get aci pg intf port

    ctx.developer = devel
    ctx.output = output
    if len(view) == 0:
        view = ['default']

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            no_cache=no_cache
        )
        if apic_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        aaep_info = False

        if 'aaep' in view:
            aaep_info = True

        policy_group_filter = []

        if name is not None:
            policy_group_filter.append(
                'name:%s' % (name)
            )

        if aaep is not None:
            policy_group_filter.append(
                'aaep:%s' % (aaep)
            )

        policy_groups = apic_handler.get_policy_groups_access_interface_port(
            policy_group_filter=policy_group_filter,
            aaep_info=aaep_info
        )

        ctx.busy = False

        if policy_groups is None or len(policy_groups) == 0:
            raise NoResultExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    policy_groups,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(policy_groups)

        if 'default' in view:
            aci_output_handler.print_policy_groups_access_interface_port_policies(
                policy_groups
            )

        if 'aaep' in view:
            aci_output_handler.print_policy_groups_access_interface_port_aaep(
                policy_groups
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
