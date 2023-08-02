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


@click.command("isis")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--domain", "domain_name", default='', callback=validations.empty_string_to_none, help="Filter by domain name")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['inst'], help="[inst|intf|lsp|nei|route|tree|tun|fault|hfault|event|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_isis_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        domain_name,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol isis"""

    # iserver get aci node proto isis

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'inst|intf|lsp|nei|route|tree|tun|fault|hfault|event|diag|all',
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

        isis_domain_filter = []
        hfault_filter = []
        event_filter = []

        if domain_name is not None:
            isis_domain_filter.append(
                'name:%s' % (domain_name)
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
        intf_info = False
        lsp_info = False
        neighbor_info = False
        route_info = False
        tree_info = False
        tunnel_info = False
        fault_info = False
        hfault_info = False
        event_info = False

        if 'inst' in view:
            instance_info = True
            domain_info = True

        if 'intf' in view:
            instance_info = True
            domain_info = True
            intf_info = True

        if 'lsp' in view:
            instance_info = True
            domain_info = True
            lsp_info = True

        if 'nei' in view:
            instance_info = True
            domain_info = True
            neighbor_info = True

        if 'route' in view:
            instance_info = True
            domain_info = True
            route_info = True

        if 'tree' in view:
            instance_info = True
            domain_info = True
            tree_info = True

        if 'tunnel' in view:
            instance_info = True
            domain_info = True
            tunnel_info = True

        if 'fault' in view:
            fault_info = True

        if 'hfault' in view:
            hfault_info = True

        if 'event' in view:
            event_info = True

        instances = []
        domains = []
        intf = []
        lsp = []
        neighbor = []
        route = []
        tree = []
        tunnels = []
        fault_record = []
        fault_inst = []
        event = []

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        for node_info in nodes_info:
            node_instance_info = apic_handler.get_protocol_isis(
                node_info['podId'],
                node_info['id'],
                isis_domain_filter=isis_domain_filter,
                instance_info=instance_info,
                domain_info=domain_info,
                interface_info=intf_info,
                lsp_info=lsp_info,
                neighbor_info=neighbor_info,
                route_info=route_info,
                tree_info=tree_info,
                tunnel_info=tunnel_info,
                fault_info=fault_info,
                hfault_info=hfault_info,
                hfault_filter=hfault_filter,
                event_info=event_info,
                event_filter=event_filter
            )

            if node_instance_info is None:
                continue

            instances.append(
                node_instance_info
            )

            if domain_info:
                domains = domains + node_instance_info['domain']

            if intf_info:
                for domain_info in node_instance_info['domain']:
                    intf = intf + domain_info['interface']

            if lsp_info:
                for domain_info in node_instance_info['domain']:
                    lsp = lsp + domain_info['lsp']

            if neighbor_info:
                for domain_info in node_instance_info['domain']:
                    neighbor = neighbor + domain_info['neighbor']

            if route_info:
                for domain_info in node_instance_info['domain']:
                    route = route + domain_info['route']

            if tree_info:
                for domain_info in node_instance_info['domain']:
                    tree = tree + domain_info['tree']

            if tunnel_info:
                for domain_info in node_instance_info['domain']:
                    tunnels = tunnels + domain_info['tunnel']

            if 'eventLog' in node_instance_info:
                if node_instance_info['eventLog'] is not None:
                    event = event + node_instance_info['eventLog']

            if 'faultRecord' in node_instance_info:
                if node_instance_info['faultRecord'] is not None:
                    fault_record = fault_record + node_instance_info['faultRecord']

            if 'faultInst' in node_instance_info:
                if node_instance_info['faultInst'] is not None:
                    fault_inst = fault_inst + node_instance_info['faultInst']

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
            aci_output_handler.print_proto_isis_instances(
                instances,
                title=True
            )

        if 'intf' in view:
            aci_output_handler.print_proto_isis_interfaces(
                intf,
                title=True
            )

        if 'lsp' in view:
            aci_output_handler.print_proto_isis_lsps(
                lsp,
                title=True
            )

        if 'neighbor' in view:
            aci_output_handler.print_proto_isis_neighbors(
                neighbor,
                title=True
            )

        if 'route' in view:
            aci_output_handler.print_proto_isis_routes(
                route,
                title=True
            )

        if 'tree' in view:
            aci_output_handler.print_proto_isis_trees(
                tree,
                title=True
            )

        if 'tunnel' in view:
            aci_output_handler.print_proto_isis_tunnels(
                tunnels,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_proto_isis_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_proto_isis_fault_record(
                fault_record,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_proto_isis_event_logs(
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
