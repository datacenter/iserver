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


@click.command("hsrp")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--vrf", "hsrp_vrf", default='', callback=validations.empty_string_to_none, help="Filter by VRF name")
@click.option("--id", "hsrp_neighbor", default='', callback=validations.empty_string_to_none, help="Filter by neighbor")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['inst'], help="[inst|dom|intf|fault|hfault|event|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_hsrp_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        hsrp_vrf,
        hsrp_neighbor,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol hsrp"""

    # iserver get aci node proto hsrp

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'inst|dom|intf|fault|hfault|event|diag|all',
        'inst',
        [
            'diag:fault,hfault,event'
        ]
    )

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            show_selected=False,
            no_cache=no_cache
        )
        if apic_handler is None:
            raise ErrorExit

        nodes_info = validations.validate_apic_node_names(
            ctx,
            apic_handler,
            node_names,
            node_role,
            pod_id=pod_id,
        )
        if nodes_info is None:
            raise ErrorExit

        hsrp_filter = []
        hfault_filter = []
        event_filter = []

        if hsrp_neighbor is not None:
            hsrp_filter.append(
                'id:%s' % (hsrp_neighbor)
            )

        if hsrp_vrf is not None:
            hsrp_filter.append(
                'vrf:%s' % (hsrp_vrf)
            )

        if fault_when is not None:
            hfault_filter.append(
                'timestamp:%s' % (fault_when)
            )
            event_filter.append(
                'timestamp:%s' % (fault_when)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        instance_info = False
        domain_info = False
        interface_info = False
        fault_info = False
        hfault_info = False
        event_info = False

        if 'inst' in view:
            instance_info = True
            domain_info = True
            interface_info = True

        if 'dom' in view:
            domain_info = True

        if 'intf' in view:
            interface_info = True

        if 'fault' in view:
            fault_info = True

        if 'hfault' in view:
            hfault_info = True

        if 'event' in view:
            event_info = True

        instances = []
        interfaces = []
        domains = []
        fault_inst = []
        fault_record = []
        event = []

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_hsrp(
                node_info['podId'],
                node_info['id'],
                hsrp_filter=hsrp_filter,
                instance_info=instance_info,
                domain_info=domain_info,
                interface_info=interface_info,
                fault_info=fault_info,
                hfault_info=hfault_info,
                hfault_filter=hfault_filter,
                event_info=event_info,
                event_filter=event_filter
            )

            if proto_info is None:
                continue

            instances.append(
                proto_info
            )

            if 'interfaces' in proto_info:
                if proto_info['interfaces'] is not None:
                    interfaces = interfaces + proto_info['interfaces']

            if 'domains' in proto_info:
                if proto_info['domains'] is not None:
                    domains = domains + proto_info['domains']

            if 'eventLog' in proto_info:
                if proto_info['eventLog'] is not None:
                    event = event + proto_info['eventLog']

            if 'faultRecord' in proto_info:
                if proto_info['faultRecord'] is not None:
                    fault_record = fault_record + proto_info['faultRecord']

            if 'faultInst' in proto_info:
                if proto_info['faultInst'] is not None:
                    fault_inst = fault_inst + proto_info['faultInst']

        event = sorted(
            event,
            key=lambda i: i['timestamp']
        )

        fault_inst = sorted(
            fault_inst,
            key=lambda i: i['timestamp']
        )

        fault_record = sorted(
            fault_record,
            key=lambda i: i['timestamp']
        )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    instances,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(instances)

        if 'inst' in view:
            aci_output_handler.print_proto_hsrp_instances(
                instances,
                title=True
            )

        if 'dom' in view:
            aci_output_handler.print_proto_hsrp_domains(
                domains,
                title=True
            )

        if 'intf' in view:
            aci_output_handler.print_proto_hsrp_interfaces(
                interfaces,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_proto_hsrp_event_logs(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_proto_hsrp_event_logs(
                fault_record,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_proto_hsrp_event_logs(
                event,
                title=True
            )

        if len(instances) == 0:
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
