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


@click.command("vpc")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--id", "vpc_domain_id", default='', callback=validations.empty_string_to_none, help="Filter by vpc domain id")
@click.option("--state", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True)
@click.option("--member", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True)
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['state'], help="[state|addr|member|vlan|fault|hfault|event|audit|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_intf_vpc_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        vpc_domain_id,
        state,
        member,
        fault,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node virtual port channel interface"""

    # iserver get aci node intf vpc

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|addr|member|vlan|fault|hfault|event|audit|diag|all',
        'state',
        [
            'diag:fault,hfault,event,audit'
        ]
    )
    if view is None:
        sys.exit(1)

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handlers = validations.validate_apic_controllers_with_nodes(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            node_names,
            node_role,
            pod_id=pod_id,
            no_cache=no_cache
        )
        if apic_handlers is None:
            raise ErrorExit

        if len(apic_handlers) == 1:
            aci_output_handler.set_apic_off()

        interface_filter = []
        hfault_filter = []
        event_filter = []
        audit_filter = []

        if vpc_domain_id is not None:
            interface_filter.append(
                'id:%s' % (vpc_domain_id)
            )

        interface_filter.append(
            'state:%s' % (state)
        )

        interface_filter.append(
            'member:%s' % (member)
        )

        if fault:
            interface_filter.append(
                'fault:any'
            )

        if fault_severity != 'any':
            hfault_filter.append(
                'severity:%s' % (fault_severity)
            )

        if fault_when is not None:
            hfault_filter.append(
                'timestamp:%s' % (fault_when)
            )
            event_filter.append(
                'timestamp:%s' % (fault_when)
            )
            audit_filter.append(
                'timestamp:%s' % (fault_when)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        fault_info = False
        hfault_info = False
        event_info = False
        audit_info = False

        if 'fault' in view:
            fault_info = True

        if 'hfault' in view:
            hfault_info = True

        if 'event' in view:
            event_info = True

        if 'audit' in view:
            audit_info = True

        interfaces = []
        members = []
        fault_record = []
        fault_inst = []
        event = []
        audit = []

        for apic_handler in apic_handlers:
            for node_info in apic_handler['nodes']:
                node_interfaces = apic_handler['handler'].get_interface_virtual_port_channel(
                    pod_id=node_info['podId'],
                    node_id=node_info['id'],
                    interface_filter=interface_filter,
                    fault_info=fault_info,
                    hfault_info=hfault_info,
                    hfault_filter=hfault_filter,
                    event_info=event_info,
                    event_filter=event_filter,
                    audit_info=audit_info,
                    audit_filter=audit_filter
                )

                if node_interfaces is None:
                    continue

                interfaces = interfaces + node_interfaces

                for interface in node_interfaces:
                    if 'eventLog' in interface:
                        if interface['eventLog'] is not None:
                            event = event + interface['eventLog']

                    if 'faultRecord' in interface:
                        if interface['faultRecord'] is not None:
                            fault_record = fault_record + interface['faultRecord']

                    if 'faultInst' in interface:
                        if interface['faultInst'] is not None:
                            fault_inst = fault_inst + interface['faultInst']

                    if 'auditLog' in interface:
                        if interface['auditLog'] is not None:
                            audit = audit + interface['auditLog']

        event = sorted(
            event,
            key=lambda i: i['timestamp']
        )

        fault_record = sorted(
            fault_record,
            key=lambda i: i['timestamp']
        )

        fault_inst = sorted(
            fault_inst,
            key=lambda i: i['timestamp']
        )

        audit = sorted(
            audit,
            key=lambda i: i['timestamp']
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    interfaces,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(interfaces)

        if 'state' in view:
            aci_output_handler.print_interfaces_virtual_port_channel_state(
                interfaces,
                title=True
            )

        if 'addr' in view:
            aci_output_handler.print_interfaces_virtual_port_channel_address(
                interfaces,
                title=True
            )

        if 'member' in view:
            aci_output_handler.print_interfaces_virtual_port_channel_member(
                members,
                title=True
            )

            aci_output_handler.print_interfaces_virtual_port_channel_vlan(
                members,
                title=False
            )

        if 'vlan' in view:
            aci_output_handler.print_interfaces_virtual_port_channel_vlan_epg(
                members,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_interface_virtual_port_channel_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_interface_virtual_port_channel_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_interface_virtual_port_channel_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'audit' in view:
            aci_output_handler.print_interface_virtual_port_channel_audit_logs(
                audit,
                when=fault_when,
                title=True
            )

        if len(interfaces) == 0:
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
