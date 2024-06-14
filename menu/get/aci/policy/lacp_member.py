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


@click.command("lacp-m")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "policy_name", default='', callback=validations.empty_string_to_none, help="Filter by policy name")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Filter by pod id")
@click.option("--node", "node_name", default='', callback=validations.empty_string_to_none, help="Filter by node name")
@click.option("--ref", "ref_policy_name", default='', callback=validations.empty_string_to_none, help="Filter by ref policy name")
@click.option("--unused", is_flag=True, show_default=True, default=False, help="Filter unused")
@click.option("--used", is_flag=True, show_default=True, default=False, help="Filter used")
@click.option("--view", "-v", type=click.Choice(['default', 'usage', 'intf', 'verbose'], case_sensitive=False), multiple=True, show_default=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_policy_port_channel_member_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        policy_name,
        pod_id,
        node_name,
        ref_policy_name,
        unused,
        used,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci policy interface port_channel_member"""

    # iserver get aci policy interface port_channel_member

    ctx.developer = devel
    ctx.output = output

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

        if len(view) == 0:
            view = ['default']

        policy_filter = []
        if policy_name is not None:
            policy_filter.append(
                'name:%s' % (policy_name)
            )

        if pod_id is not None:
            policy_filter.append(
                'pod:%s' % (pod_id)
            )

        if node_name is not None:
            policy_filter.append(
                'node:%s' % (node_name)
            )

        if ref_policy_name is not None:
            policy_filter.append(
                'ref_policy_name:%s' % (ref_policy_name)
            )

        if used:
            policy_filter.append(
                'used:true'
            )

        if unused:
            policy_filter.append(
                'used:false'
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        policies = apic_handler.get_policy_interface_port_channel_member(
            policy_filter=policy_filter,
            attachment_info=True
        )

        context_name = apic_handler.set_policy_interface_port_channel_member_context(
            policies
        )

        ctx.busy = False

        if policies is None or len(policies) == 0:
            raise NoResultExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    policies,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(policies)

        if 'default' in view:
            aci_output_handler.print_policies_interface_port_channel_member_summary(
                policies
            )

        if 'usage' in view:
            aci_output_handler.print_policies_interface_port_channel_member_usage(
                policies
            )

        if 'intf' in view:
            aci_output_handler.print_policies_interface_port_channel_member_interfaces(
                policies
            )

        if 'verbose' in view:
            for policy in policies:
                aci_output_handler.print_policy_interface_port_channel_member(
                    policy
                )

        if context_name is not None:
            ctx.my_output.default('Context: %s' % (context_name))

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
