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


@click.command("pc")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--id", "port_channel_id", default='', callback=validations.empty_string_to_none, help="Filter by port channel id")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--speed", default='', callback=validations.empty_string_to_none, help="Filter by speed")
@click.option("--domain", default='', callback=validations.empty_string_to_none, help="Filter by domain id")
@click.option("--state", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True, help="Filter by state")
@click.option("--view", "-v", type=click.Choice(['default', 'port', 'verbose'], case_sensitive=False), multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_intf_pc_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        port_channel_id,
        name,
        speed,
        domain,
        state,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node port channel interface"""

    # iserver get aci node intf pc

    ctx.developer = devel
    ctx.output = output
    if len(view) == 0:
        view = ['default']

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
        if port_channel_id is not None:
            interface_filter.append(
                'id:%s' % (port_channel_id)
            )

        if name is not None:
            interface_filter.append(
                'name:%s' % (name)
            )

        if speed is not None:
            interface_filter.append(
                'speed:%s' % (speed)
            )

        if domain is not None:
            interface_filter.append(
                'domain:%s' % (domain)
            )

        interface_filter.append(
            'state:%s' % (state)
        )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        instance_info = False
        members_info = False
        if 'verbose' in view:
            members_info = True
            instance_info = True

        interfaces = []
        for apic_handler in apic_handlers:
            for node_info in apic_handler['nodes']:
                node_interfaces = apic_handler['handler'].get_interface_port_channel(
                    pod_id=node_info['podId'],
                    node_id=node_info['id'],
                    interface_port_channel_filter=interface_filter,
                    vpc_domain_info=True,
                    members_info=members_info,
                    instance_info=instance_info
                )

                if node_interfaces is None:
                    continue

                interfaces = interfaces + node_interfaces

        ctx.busy = False

        if len(interfaces) == 0:
            raise NoResultExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    interfaces,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(interfaces)

        if 'default' in view:
            aci_output_handler.print_interfaces_port_channel_state(
                interfaces
            )

        if 'port' in view:
            aci_output_handler.print_interfaces_port_channel_port(
                interfaces
            )

        if 'verbose' in view:
            for interface in interfaces:
                aci_output_handler.print_interfaces_port_channel_state(
                    [interface]
                )
                aci_output_handler.print_interface_port_channel(
                    interface
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
