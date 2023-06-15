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
@click.option("--view", "-v", type=click.Choice(['default', 'instance', 'verbose'], case_sensitive=False), multiple=True, show_default=False)
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
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol bfd"""

    # iserver get aci node proto bfd

    ctx.developer = devel
    ctx.output = output
    if len(view) == 0:
        view = ['default']

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

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        sessions = []
        instances = []

        session_info = False
        if 'verbose' in view:
            session_info = True

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_bfd(
                node_info['podId'],
                node_info['id'],
                bfd_filter=bfd_filter,
                session_info=session_info
            )

            if proto_info is None:
                continue

            sessions = sessions + proto_info['sessions']
            instances.append(
                proto_info
            )

        ctx.busy = False

        if len(instances) == 0:
            raise NoResultExit

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

        if 'default' in view:
            aci_output_handler.print_proto_bfd_sessions(
                sessions
            )

        if 'instance' in view:
            aci_output_handler.print_proto_bfd_instances(
                instances
            )

        if 'verbose' in view:
            for session in sessions:
                aci_output_handler.print_proto_bfd_session(
                    session
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
