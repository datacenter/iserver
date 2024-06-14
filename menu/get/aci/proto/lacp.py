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


@click.command("lacp")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--mac", default='', callback=validations.empty_string_to_none, help="Filter by mac address")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['intf'], help="[inst|intf|stats|event|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_lacp_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        mac,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol lacp"""

    # iserver get aci node proto lacp

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'inst|intf|stats|event|all',
        'intf',
        []
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

        event_filter = []
        if fault_when is not None:
            event_filter.append(
                'timestamp:%s' % (fault_when)
            )

        instance_info = False
        interface_info = False
        event_info = False

        if 'inst' in view:
            instance_info = True
            interface_info = True

        if 'intf' in view:
            instance_info = True
            interface_info = True

        if 'stats' in view:
            instance_info = True
            interface_info = True

        if 'event' in view:
            event_info = True

        instances = []
        interfaces = []
        event = []

        interface_filter = []
        if mac is not None:
            interface_filter.append(
                'mac:%s' % (mac)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_lacp(
                node_info['podId'],
                node_info['id'],
                instance_info=instance_info,
                interface_info=interface_info,
                interface_filter=interface_filter,
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

            if 'eventLog' in proto_info:
                if proto_info['eventLog'] is not None:
                    event = event + proto_info['eventLog']

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
            aci_output_handler.print_proto_lacp_instances(
                instances,
                title=True
            )

        if 'intf' in view:
            aci_output_handler.print_proto_lacp_interfaces(
                interfaces,
                title=True
            )

        if 'stats' in view:
            aci_output_handler.print_proto_lacp_interfaces_stats(
                interfaces,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_proto_lacp_event_logs(
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
