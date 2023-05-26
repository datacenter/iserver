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


@click.command("mgmt")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--output", "-o", type=click.Choice(['state', 'addr', 'nei', 'verbose', 'json'], case_sensitive=False), default='state', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_intf_mgmt_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        output,
        devel
        ):
    """Get aci node management interface"""

    # iserver get aci node intf mgmt

    ctx.developer = devel
    if output == 'json':
        ctx.output = 'json'
    else:
        ctx.output = 'default'

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handlers = validations.validate_apic_controllers_with_nodes(
            ctx,
            controller,
            controller_ip,
            controller_username,
            controller_password,
            node_names,
            node_role,
            pod_id=pod_id
        )
        if apic_handlers is None:
            raise ErrorExit

        if len(apic_handlers) == 1:
            aci_output_handler.set_apic_off()

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        cdp_info = False
        lldp_info = False
        faults_info = False
        state_info = True
        stats_info = False

        if output in ['verbose', 'json']:
            cdp_info = True
            lldp_info = True
            faults_info = True
            stats_info = True

        if output == 'nei':
            cdp_info = True
            lldp_info = True

        if output == 'addr':
            stats_info = True

        interfaces = []
        for apic_handler in apic_handlers:
            for node_info in apic_handler['nodes']:
                node_interfaces = apic_handler['handler'].get_interface_management(
                    node_info['podId'],
                    node_info['id'],
                    cdp_info=cdp_info,
                    lldp_info=lldp_info,
                    faults_info=faults_info,
                    state_info=state_info,
                    stats_info=stats_info
                )

                interfaces = interfaces + node_interfaces

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    interfaces,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(interfaces)

        if output == 'state':
            aci_output_handler.print_interfaces_management_state(
                interfaces
            )

        if output == 'addr':
            aci_output_handler.print_interfaces_management_address(
                interfaces
            )

        if output == 'nei':
            aci_output_handler.print_interfaces_management_neighbor(
                interfaces
            )

        if output == 'verbose':
            for interface in interfaces:
                aci_output_handler.print_interface_management(
                    interface
                )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
