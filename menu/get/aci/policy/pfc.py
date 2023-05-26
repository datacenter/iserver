import sys
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


@click.command("pfc")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "pfc_policy_name", default='', help="Priority Flow Control Policy Name")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_name", default='', help="Node Name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_policy_pfc_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        pfc_policy_name,
        pod_id,
        node_name,
        output,
        verbose,
        devel
        ):
    """Get aci policy interface priority flow control (pfc)"""

    # iserver get aci policy interface pfc

    ctx.developer = devel
    ctx.output = output

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

        if len(node_name) > 0:
            node_info = validations.validate_apic_node_name(
                ctx,
                apic_handler,
                node_name,
                pod_id=pod_id
            )
            if node_info is None:
                raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if len(node_name) > 0:
            ports = apic_handler.get_ports(
                node_info['podId'],
                node_info['id']
            )
            node_policy = apic_handler.get_policy_interface_pfc_node(
                node_info['id'],
                ports
            )

            ctx.busy = False

            aci_output_handler.print_policy_interface_pfc_node(
                node_policy
            )

            ctx.my_output.json_output(node_policy)

        if len(node_name) == 0 and len(pfc_policy_name) == 0:
            policy = apic_handler.get_policy_interface_pfc()

            ctx.busy = False

            aci_output_handler.print_policies_interface_pfc(
                policy,
                verbose=verbose
            )

            ctx.my_output.json_output(policy)

        if len(node_name) == 0 and len(pfc_policy_name) > 0:
            policy = apic_handler.get_policy_interface_pfc(pfc_policy_name=pfc_policy_name)
            if verbose:
                for node in policy['nodeInterfaces']:
                    ports = apic_handler.get_ports(
                        node['pod_id'],
                        node['node_id']
                    )
                    node['interfaces'] = apic_handler.get_policy_interface_pfc_node(
                        node['node_id'],
                        ports,
                        pfc_policy_name=pfc_policy_name
                    )

            ctx.busy = False

            aci_output_handler.print_policy_interface_pfc(
                policy,
                verbose=verbose
            )

            ctx.my_output.json_output(policy)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
