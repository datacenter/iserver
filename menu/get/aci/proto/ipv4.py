import sys
import json
import traceback
import copy
import threading
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


@click.command("ipv4")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--vrf", "vrf_name", default='', callback=validations.empty_string_to_none, help="VRF")
@click.option("--type", "route_filter", type=click.Choice(['ibgp', 'ebgp', 'bgp', 'static', 'local', 'direct'], case_sensitive=False), multiple=True)
@click.option("--address", "ip_address_filter", default='', callback=validations.validate_ip, help="IP Address filter")
@click.option("--subnet", "ip_subnet_filter", default='', callback=validations.validate_ip_subnet, help="IP Subnet filter")
@click.option("--longer", "longer_prefixes", is_flag=True, show_default=True, default=False, help="Match longer prefixes")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['route'], help="[inst|dom|route|fault|hfault|event|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_ipv4_command(
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
        route_filter,
        ip_address_filter,
        ip_subnet_filter,
        longer_prefixes,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol ipv4"""

    # iserver get aci node proto ipv4

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'inst|dom|route|fault|hfault|event|diag|all',
        'route',
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

        ipv4_filter = []
        hfault_filter = []
        event_filter = []

        if vrf_name is not None:
            ipv4_filter.append(
                'vrf:%s' % (vrf_name)
            )

        if len(route_filter) > 0:
            for item in route_filter:
                ipv4_filter.append(
                    item
                )

        if ip_address_filter is not None:
            if len(ip_address_filter) > 0:
                ipv4_filter.append(
                    'ip:%s' % (ip_address_filter)
                )

        if ip_subnet_filter is not None:
            if len(ip_subnet_filter) > 0:
                if longer_prefixes:
                    ipv4_filter.append(
                        'subnet-longer:%s' % (ip_subnet_filter)
                    )
                else:
                    ipv4_filter.append(
                        'subnet:%s' % (ip_subnet_filter)
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
        route_info = False
        fault_info = False
        hfault_info = False
        event_info = False

        if 'inst' in view:
            instance_info = True
            domain_info = True
            route_info = True

        if 'dom' in view:
            domain_info = True
            route_info = True

        if 'route' in view:
            domain_info = True
            route_info = True

        if 'fault' in view:
            fault_info = True
            domain_info = True

        if 'hfault' in view:
            hfault_info = True
            domain_info = True

        if 'event' in view:
            event_info = True
            domain_info = True

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        proto_infos = []
        instance = []
        domain = []
        route = []
        fault_record = []
        fault_inst = []
        event = []

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_ipv4(
                node_info['podId'],
                node_info['id'],
                ipv4_filter=ipv4_filter,
                instance_info=instance_info,
                domain_info=domain_info,
                route_info=route_info,
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

            if 'route' in proto_info:
                if proto_info['route'] is not None:
                    route = route + proto_info['route']

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
            aci_output_handler.print_proto_ipv4_instances(
                instance,
                title=True
            )

        if 'dom' in view:
            aci_output_handler.print_proto_ipv4_domains(
                domain,
                title=True
            )

        if 'route' in view:
            aci_output_handler.print_proto_ipv4_routes(
                route,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_proto_ipv4_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_proto_ipv4_fault_record(
                fault_record,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_proto_ipv4_event_logs(
                event,
                title=True
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
