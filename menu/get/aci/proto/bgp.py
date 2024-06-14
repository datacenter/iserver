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


@click.command("bgp")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--asn", "bgp_asn", default='', callback=validations.empty_string_to_none, help="Filter by BGP ASN")
@click.option("--vrf", "bgp_vrf", default='', callback=validations.empty_string_to_none, help="Filter by VRF name")
@click.option("--rtr-ip", "rtr_ip_address", default='', callback=validations.validate_ip, help="Filter by BGP Router IP address")
@click.option("--rtr-subnet", "rtr_ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by BGP Router IP subnet")
@click.option("--nbr-type", "nbr_type", type=click.Choice(['any', 'ibgp', 'ebgp'], case_sensitive=False), default='any', show_default=True, help="Filter by BGP neighbor type")
@click.option("--nbr-ip", "nbr_ip_address", default='', callback=validations.validate_ip, help="Filter by BPG Neighbor IP address")
@click.option("--nbr-subnet", "nbr_ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by BPG Neighbor IP subnet")
@click.option("--nbr-state", "nbr_state", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True, help="Filter by BGP neighbor state")
@click.option("--intf", "source_interface", default='', callback=validations.empty_string_to_none, help="Filter by BGP Neighbor source interface")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['nei'], help="[inst|vrf|nei|peer|route|fault|hfault|event|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_bgp_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        bgp_asn,
        bgp_vrf,
        rtr_ip_address,
        rtr_ip_subnet,
        nbr_type,
        nbr_ip_address,
        nbr_ip_subnet,
        nbr_state,
        source_interface,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol bgp"""

    # iserver get aci node proto bgp

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'inst|vrf|nei|peer|route|fault|hfault|event|diag|all',
        'nei',
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
            pod_id=pod_id
        )
        if nodes_info is None:
            raise ErrorExit

        bgp_filter = []
        hfault_filter = []
        event_filter = []

        if bgp_asn is not None:
            bgp_filter.append(
                'asn:%s' % (bgp_asn)
            )

        if bgp_vrf is not None:
            bgp_filter.append(
                'vrf:%s' % (bgp_vrf)
            )
            hfault_filter.append(
                'domainNameT:%s' % (bgp_vrf)
            )
            event_filter.append(
                'domainNameT:%s' % (bgp_vrf)
            )

        if len(rtr_ip_address) > 0:
            bgp_filter.append(
                'rtr-ip:%s' % (rtr_ip_address)
            )

        if len(rtr_ip_subnet) > 0:
            bgp_filter.append(
                'rtr-subnet:%s' % (rtr_ip_subnet)
            )

        if len(nbr_type) > 0:
            bgp_filter.append(
                'nbr-type:%s' % (nbr_type)
            )

        if len(nbr_ip_address) > 0:
            bgp_filter.append(
                'nbr-ip:%s' % (nbr_ip_address)
            )

        if len(nbr_ip_subnet) > 0:
            bgp_filter.append(
                'nbr-subnet:%s' % (nbr_ip_subnet)
            )

        if nbr_state is not None:
            bgp_filter.append(
                'state:%s' % (nbr_state)
            )

        if source_interface is not None:
            bgp_filter.append(
                'interface:%s' % (source_interface)
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

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        instance_info = False
        domain_info = False
        neighbor_info = False
        stats_info = False
        prefix_info = False
        fault_info = False
        hfault_info = False
        event_info = False

        if 'inst' in view:
            instance_info = True
            domain_info = True
            neighbor_info = True

        if 'vrf' in view:
            instance_info = True
            domain_info = True
            neighbor_info = True

        if 'nei' in view:
            instance_info = True
            domain_info = True
            neighbor_info = True
            stats_info = True

        if 'peer' in view:
            instance_info = True
            domain_info = True
            neighbor_info = True
            stats_info = True

        if 'route' in view:
            instance_info = True
            domain_info = True
            neighbor_info = True
            stats_info = True
            prefix_info = True

        if 'fault' in view:
            fault_info = True

        if 'hfault' in view:
            hfault_info = True

        if 'event' in view:
            event_info = True

        proto_infos = []
        instance = []
        domain = []
        neighbor = []
        route = []
        fault_record = []
        fault_inst = []
        event = []

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_bgp(
                node_info['podId'],
                node_info['id'],
                bgp_filter=bgp_filter,
                instance_info=instance_info,
                domain_info=domain_info,
                neighbor_info=neighbor_info,
                stats_info=stats_info,
                prefix_info=prefix_info,
                fault_info=fault_info,
                hfault_info=hfault_info,
                hfault_filter=hfault_filter,
                event_info=event_info,
                event_filter=event_filter
            )

            if proto_info is None:
                continue

            proto_infos.append(
                proto_info
            )

            if 'instance' in proto_info:
                if proto_info['instance'] is not None:
                    instance.append(
                        proto_info['instance']
                    )

            if 'domain' in proto_info:
                if proto_info['domain'] is not None:
                    domain = domain + proto_info['domain']

            if 'neighbor' in proto_info:
                if proto_info['neighbor'] is not None:
                    neighbor = neighbor + proto_info['neighbor']

                    if prefix_info:
                        for neighbor_info in proto_info['neighbor']:
                            if 'route' in neighbor_info:
                                if neighbor_info['route'] is not None:
                                    route = route + neighbor_info['route']

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
                    proto_infos,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(proto_infos)

        if 'inst' in view:
            aci_output_handler.print_proto_bgp_instances(
                instance,
                title=True
            )

        if 'vrf' in view:
            aci_output_handler.print_proto_bgp_domains(
                domain,
                title=True
            )

        if 'nei' in view:
            aci_output_handler.print_proto_bgp_neighbors(
                neighbor,
                title=True
            )


        if 'peer' in view:
            aci_output_handler.print_proto_bgp_peers(
                neighbor
            )

        if 'route' in view:
            aci_output_handler.print_proto_ipv4_routes(
                route
            )

        if 'fault' in view:
            aci_output_handler.print_proto_bgp_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_proto_bgp_fault_record(
                fault_record,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_proto_bgp_event_logs(
                event,
                title=True
            )

        ctx.my_output.default('Filter: node, role, asn, vrf, rtr-ip, rtr-subnet, type, nbr-type, nbr-ip, nbr-subnet, nbr-state, intf, severity, when', before_newline=True)
        ctx.my_output.default('View:   inst, vrf, nei (def), peer, route, fault, hfault, event, diag, all')

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
