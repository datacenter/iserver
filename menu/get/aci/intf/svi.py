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


@click.command("svi")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--id", "port_name", default='', callback=validations.empty_string_to_none, help="Port name")
@click.option("--admin", "admin_state", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True)
@click.option("--oper", "oper_state", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True)
@click.option("--type", "vlan_type", type=click.Choice(['any', 'int', 'ext'], case_sensitive=False), default='any', show_default=True)
@click.option("--mac", "mac_address", default='', callback=validations.empty_string_to_none, help="MAC Address filter")
@click.option("--vlan", default='', callback=validations.empty_string_to_none, help="VLAN filter")
@click.option("--address", "ip_address", default='', callback=validations.validate_ip, help="IP Address filter")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="IP Subnet filter")
@click.option("--view", "-v", type=click.Choice(['default', 'addr', 'counter', 'verbose'], case_sensitive=False), multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_intf_svi_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        port_name,
        admin_state,
        oper_state,
        vlan_type,
        mac_address,
        vlan,
        ip_address,
        ip_subnet,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node svi interface"""

    # iserver get aci node intf svi

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
        if port_name is not None:
            interface_filter.append(
                'id:%s' % (port_name)
            )

        interface_filter.append(
            'admin:%s' % (admin_state)
        )

        interface_filter.append(
            'oper:%s' % (oper_state)
        )

        interface_filter.append(
            'type:%s' % (vlan_type)
        )

        if mac_address is not None:
            interface_filter.append(
                'mac:%s' % (mac_address)
            )

        if vlan is not None:
            interface_filter.append(
                'vlan:%s' % (vlan)
            )

        if len(ip_subnet) > 0:
            interface_filter.append(
                'subnet:%s' % (ip_subnet)
            )

        if len(ip_address) > 0:
            interface_filter.append(
                'ip:%s' % (ip_address)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        interfaces = []
        for apic_handler in apic_handlers:
            for node_info in apic_handler['nodes']:
                node_interfaces = apic_handler['handler'].get_interfaces_svi(
                    node_info['podId'],
                    node_info['id'],
                    interface_filter=interface_filter
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
            aci_output_handler.print_interfaces_svi_state(
                interfaces
            )

        if 'addr' in view:
            aci_output_handler.print_interfaces_svi_address(
                interfaces
            )

        if 'counter' in view:
            aci_output_handler.print_interfaces_svi_counter(
                interfaces
            )

        if 'verbose' in view:
            for interface in interfaces:
                aci_output_handler.print_interface_svi(
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
