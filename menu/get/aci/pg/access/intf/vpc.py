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


@click.command("vpc")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--aaep", default='', callback=validations.empty_string_to_none, help="Filter by aaep")
@click.option("--policy", default='', callback=validations.empty_string_to_none, help="Filter by policy")
@click.option("--output", "-o", type=click.Choice(['policy', 'aaep', 'node', 'port', 'json'], case_sensitive=False), default='policy', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_pg_access_interface_vpc_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        name,
        aaep,
        policy,
        output,
        devel
        ):
    """Get aci policy group interface vpc"""

    # iserver get aci pg intf vpc

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

        node_info = False
        port_info = False
        aaep_info = False

        if output == 'node':
            node_info = True

        if output == 'port':
            node_info = True
            port_info = True

        if output == 'aaep':
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

        if policy is not None:
            policy_group_filter.append(
                'policy:%s' % (policy)
            )

        policy_groups = apic_handler.get_policy_groups_access_interface_vpc(
            policy_group_filter=policy_group_filter,
            node_info=node_info,
            port_info=port_info,
            aaep_info=aaep_info
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    policy_groups,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(policy_groups)

        if output == 'policy':
            aci_output_handler.print_policy_groups_access_interface_vpc_policies(
                policy_groups
            )

        if output == 'node':
            aci_output_handler.print_policy_groups_access_interface_vpc_nodes(
                policy_groups
            )

        if output == 'port':
            aci_output_handler.print_policy_groups_access_interface_vpc_ports(
                policy_groups
            )

        if output == 'aaep':
            aci_output_handler.print_policy_groups_access_interface_vpc_aaep(
                policy_groups
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
