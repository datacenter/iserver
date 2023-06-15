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


@click.command("vpc")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--id", "vpc_domain_id", default='', callback=validations.empty_string_to_none, help="Filter by vpc domain id")
@click.option("--state", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True)
@click.option("--member", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True)
@click.option("--view", "-v", type=click.Choice(['default', 'address', 'verbose'], case_sensitive=False), multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_intf_vpc_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        vpc_domain_id,
        state,
        member,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node virtual port channel interface"""

    # iserver get aci node intf vpc

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
        if vpc_domain_id is not None:
            interface_filter.append(
                'id:%s' % (vpc_domain_id)
            )

        interface_filter.append(
            'state:%s' % (state)
        )

        interface_filter.append(
            'member:%s' % (member)
        )

        members_info = True
        if 'address' in view and member == 'any':
            members_info = False

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        interfaces = []
        for apic_handler in apic_handlers:
            for node_info in apic_handler['nodes']:
                node_interfaces = apic_handler['handler'].get_interface_virtual_port_channel(
                    pod_id=node_info['podId'],
                    node_id=node_info['id'],
                    interface_filter=interface_filter,
                    members_info=members_info
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
            aci_output_handler.print_interfaces_virtual_port_channel_state(
                interfaces
            )

        if 'address' in view:
            aci_output_handler.print_interfaces_virtual_port_channel_address(
                interfaces
            )

        if 'verbose' in view:
            for interface in interfaces:
                aci_output_handler.print_interfaces_virtual_port_channel_state(
                    [interface]
                )
                aci_output_handler.print_interface_virtual_port_channel(
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
