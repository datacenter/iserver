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


@click.command("arp")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--vrf", "vrf_name", default='', callback=validations.empty_string_to_none, help="Filter by VRF name")
@click.option("--mac", "mac_address", default='', callback=validations.empty_string_to_none, help="Filter by MAC address")
@click.option("--ip", "ip_address", default='', callback=validations.validate_ip, help="Filter by IP")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by subnet")
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['adj'], help="[inst|dom|adj|fault|hfault|event|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_arp_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        vrf_name,
        mac_address,
        ip_address,
        ip_subnet,
        fault,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol arp"""

    # iserver get aci node proto arp

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'inst|dom|adj|fault|hfault|event|diag|all',
        'adj',
        [
            'diag:fault,hfault,event'
        ]
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

        arp_domain_filter = []
        hfault_filter = []
        event_filter = []

        if vrf_name is not None:
            arp_domain_filter.append(
                'name:%s' % (vrf_name)
            )

        if mac_address is not None:
            arp_domain_filter.append(
                'mac:%s' % (mac_address)
            )

        if len(ip_address) > 0:
            arp_domain_filter.append(
                'ip:%s' % (ip_address)
            )

        if len(ip_subnet) > 0:
            arp_domain_filter.append(
                'subnet:%s' % (ip_subnet)
            )

        if fault:
            arp_domain_filter.append(
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

        instance_info = False
        domain_info = False
        adjacency_info = False
        interface_info = False
        fault_info = False
        hfault_info = False
        event_info = False

        if 'inst' in view:
            instance_info = True

        if 'dom' in view:
            domain_info = True
            adjacency_info = True

        if 'adj' in view:
            domain_info = True
            adjacency_info = True
            interface_info = True

        if 'fault' in view:
            fault_info = True

        if 'hfault' in view:
            hfault_info = True

        if 'event' in view:
            event_info = True

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        proto_infos = []
        instance = []
        domain = []
        adjacency = []
        interface = []
        fault_record = []
        fault_inst = []
        event = []

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_arp(
                node_info['podId'],
                node_info['id'],
                arp_domain_filter=arp_domain_filter,
                instance_info=instance_info,
                domain_info=domain_info,
                adjacency_info=adjacency_info,
                interface_info=interface_info,
                fault_info=fault_info,
                hfault_info=hfault_info,
                hfault_filter=hfault_filter,
                event_info=event_info,
                event_filter=event_filter
            )

            if proto_info is None:
                continue

            if 'instance' in proto_info:
                if proto_info['instance'] is not None:
                    instance.append(
                        proto_info['instance']
                    )

            if 'domain' in proto_info:
                if proto_info['domain'] is not None:
                    domain = domain + proto_info['domain']

            if 'interface' in proto_info:
                if proto_info['interface'] is not None:
                    interface = interface + proto_info['interface']

            if 'adjacency' in proto_info:
                if proto_info['adjacency'] is not None:
                    adjacency = adjacency + proto_info['adjacency']

            if 'eventLog' in proto_info:
                if proto_info['eventLog'] is not None:
                    event = event + proto_info['eventLog']

            if 'faultRecord' in proto_info:
                if proto_info['faultRecord'] is not None:
                    fault_record = fault_record + proto_info['faultRecord']

            if 'faultInst' in proto_info:
                if proto_info['faultInst'] is not None:
                    fault_inst = fault_inst + proto_info['faultInst']

            proto_infos.append(
                proto_info
            )

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
                    proto_infos,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(proto_infos)

        if 'inst' in view:
            aci_output_handler.print_proto_arp_instances(
                instance,
                title=True
            )

        if 'dom' in view:
            aci_output_handler.print_proto_arp_domains(
                domain,
                title=True
            )

        if 'adj' in view:
            aci_output_handler.print_proto_arp_adjacencies(
                adjacency,
                title=True
            )

            aci_output_handler.print_proto_arp_interface_summary(
                interface,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_proto_arp_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_proto_arp_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_proto_arp_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if len(proto_infos) == 0:
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
