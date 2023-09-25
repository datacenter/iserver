import sys
import json
import threading
import traceback
import click

from lib import context
from lib import ip_helper
from lib.aci import output as aci_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("lldp")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--device", default='', callback=validations.empty_string_to_none, help="Filter neighbor by device name")
@click.option("--mac", default='', callback=validations.empty_string_to_none, help="Filter neighbor by mac address")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['nei'], help="[inst|nei|stats|fault|hfault|event|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_lldp_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        device,
        mac,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol lldp"""

    # iserver get aci node proto lldp

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'inst|nei|stats|fault|hfault|event|diag|all',
        'nei',
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

        context_handler = context.Context(log_id=ctx.run_id)
        lldp_context = None
        if controller is not None:
            lldp_context = context_handler.initialize_apic(
                controller['name']
            )

        adjacency_filter = []
        hfault_filter = []
        event_filter = []

        if device is not None:
            adjacency_filter.append(
                'device:%s' % (device)
            )

        if mac is not None:
            adjacency_filter.append(
                'mac:%s' % (mac)
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
        stats_info = False
        adjacency_info = False
        fault_info = False
        hfault_info = False
        event_info = False

        if 'inst' in view:
            instance_info = True
            stats_info = True
            adjacency_info = True

        if 'stats' in view:
            stats_info = True

        if 'nei' in view:
            adjacency_info = True

        if 'fault' in view:
            fault_info = True
            adjacency_info = True

        if 'hfault' in view:
            hfault_info = True
            adjacency_info = True

        if 'event' in view:
            event_info = True
            adjacency_info = True

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        proto_infos = []
        instance = []
        stats = []
        adjacency = []
        fault_record = []
        fault_inst = []
        event = []

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_lldp(
                node_info['podId'],
                node_info['id'],
                adjacency_filter=adjacency_filter,
                instance_info=instance_info,
                stats_info=stats_info,
                adjacency_info=adjacency_info,
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

            if instance_info and proto_info['instance'] is not None:
                instance.append(
                    proto_info['instance']
                )

            if stats_info and proto_info['stats'] is not None:
                stats.append(
                    proto_info['stats']
                )

            if adjacency_info and proto_info['adjacency'] is not None:
                adjacency = adjacency + proto_info['adjacency']
                lldp_context = apic_handler.add_protocol_lldp_adjacency_context(
                    lldp_context,
                    adjacency
                )

                for lldp_adjacency_info in proto_info['adjacency']:
                    if 'eventLog' in lldp_adjacency_info:
                        if lldp_adjacency_info['eventLog'] is not None:
                            event = event + lldp_adjacency_info['eventLog']

                    if 'faultInst' in lldp_adjacency_info:
                        if lldp_adjacency_info['faultInst'] is not None:
                            fault_inst = fault_inst + lldp_adjacency_info['faultInst']

                    if 'faultRecord' in lldp_adjacency_info:
                        if lldp_adjacency_info['faultRecord'] is not None:
                            fault_record = fault_record + lldp_adjacency_info['faultRecord']

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
            aci_output_handler.print_proto_lldp_instance(
                instance,
                title=True
            )

        if 'stats' in view:
            aci_output_handler.print_proto_lldp_instances_stats(
                stats,
                title=True
            )

        if 'nei' in view:
            aci_output_handler.print_lldp_adjacency_endpoints(
                adjacency,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_proto_lldp_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_proto_lldp_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_proto_lldp_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if context_handler.is_interface_defined(lldp_context):
            success = context_handler.set(
                'lldp',
                lldp_context
            )
            if success:
                ctx.my_output.default('Interface context: lldp')

        if len(instance) == 0 and len(stats) == 0 and len(adjacency) == 0:
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
