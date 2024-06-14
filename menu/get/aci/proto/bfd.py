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


@click.command("bfd")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--id", "session_id", default='', callback=validations.empty_string_to_none, help="Filter by session id")
@click.option("--intf", "interface_id", default='', callback=validations.empty_string_to_none, help="Filter by interface id")
@click.option("--state", "session_state", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True, help="Filter by session state")
@click.option("--vrf", "vrf_name", default='', callback=validations.empty_string_to_none, help="Filter by VRF name")
@click.option("--address", "ip_address", default='', callback=validations.validate_ip, help="Filter by IP address")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by IP subnet")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['session'], help="[inst|session|fault|hfault|event|diag|all|verbose]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_bfd_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        session_id,
        interface_id,
        session_state,
        vrf_name,
        ip_address,
        ip_subnet,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol bfd"""

    # iserver get aci node proto bfd

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'inst|session|fault|hfault|event|diag|all|verbose',
        'session',
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

        bfd_filter = []
        hfault_filter = []
        event_filter = []

        if session_id is not None:
            bfd_filter.append(
                'session_id:%s' % (session_id)
            )

        if interface_id is not None:
            bfd_filter.append(
                'interface_id:%s' % (interface_id)
            )

        if session_state is not None:
            bfd_filter.append(
                'session_state:%s' % (session_state)
            )

        if vrf_name is not None:
            bfd_filter.append(
                'vrf:%s' % (vrf_name)
            )

        if len(ip_address) > 0:
            bfd_filter.append(
                'ip:%s' % (ip_address)
            )

        if len(ip_subnet) > 0:
            bfd_filter.append(
                'subnet:%s' % (ip_subnet)
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

        sessions = []
        instances = []
        fault_record = []
        fault_inst = []
        event = []

        instance_info = False
        session_info = False
        interface_info = False
        fault_info = False
        hfault_info = False
        event_info = False

        if 'inst' in view:
            instance_info = True
            session_info = True
            interface_info = True

        if 'session' in view:
            session_info = True

        if 'fault' in view:
            fault_info = True
            session_info = True

        if 'hfault' in view:
            hfault_info = True
            session_info = True

        if 'event' in view:
            event_info = True
            session_info = True

        if 'verbose' in view:
            instance_info = True
            session_info = True
            interface_info = True
            fault_info = True
            hfault_info = True
            event_info = True

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_bfd(
                node_info['podId'],
                node_info['id'],
                bfd_filter=bfd_filter,
                instance_info=instance_info,
                session_info=session_info,
                interface_info=interface_info,
                fault_info=fault_info,
                hfault_info=hfault_info,
                hfault_filter=hfault_filter,
                event_info=event_info,
                event_filter=event_filter
            )

            if proto_info is None:
                continue

            sessions = sessions + proto_info['sessions']

            instances.append(
                proto_info
            )

            for session in sessions:
                if 'eventLog' in session:
                    if session['eventLog'] is not None:
                        event = event + session['eventLog']

                if 'faultInst' in session:
                    if session['faultInst'] is not None:
                        fault_inst = fault_inst + session['faultInst']

                if 'faultRecord' in session:
                    if session['faultRecord'] is not None:
                        fault_record = fault_record + session['faultRecord']

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
            aci_output_handler.print_proto_bfd_instances(
                instances
            )

        if 'session' in view:
            aci_output_handler.print_proto_bfd_sessions(
                sessions,
                title=True
            )

            aci_output_handler.print_proto_bfd_sessions_stats(
                sessions,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_proto_bfd_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_proto_bfd_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_proto_bfd_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'verbose' in view:
            for session in sessions:
                aci_output_handler.print_proto_bfd_session(
                    session,
                    when=fault_when
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
