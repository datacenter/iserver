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


@click.command("node")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--role", "node_role", type=click.Choice(['any', 'controller', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--id", "node_id", default='', callback=validations.empty_string_to_none, help="Filter by node id")
@click.option("--name", "node_name", default='', callback=validations.empty_string_to_none, help="Filter by node name")
@click.option("--model", default='', callback=validations.empty_string_to_none, help="Filter by model")
@click.option("--address", "ip_address", default='', callback=validations.validate_ip, help="Filter by subnet with IP")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by subnet within subnet")
@click.option("--view", "-v", default=['state'], help="[state|intf|ip|power|psu|sensor|temp|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        node_role,
        pod_id,
        node_id,
        node_name,
        model,
        ip_address,
        ip_subnet,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node"""

    # iserver get aci node

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|intf|ip|power|psu|sensor|temp|all',
        'state',
        []
    )

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handlers = validations.validate_apic_controllers(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            no_cache=no_cache
        )
        if apic_handlers is None:
            raise ErrorExit

        if len(apic_handlers) == 1:
            aci_output_handler.set_apic_off()

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        power_info = False
        psu_info = False
        sensor_info = False
        temp_info = False
        system_info = False

        node_filter = []
        if node_id is not None:
            node_filter.append(
                'id:%s' % (node_id)
            )

        if node_name is not None:
            node_filter.append(
                'name:%s' % (node_name)
            )

        if pod_id is not None:
            node_filter.append(
                'pod:%s' % (pod_id)
            )

        if node_role != 'any':
            node_filter.append(
                'role:%s' % (node_role)
            )

        if model is not None:
            node_filter.append(
                'model:%s' % (model)
            )

        if len(ip_subnet) > 0:
            system_info = True
            node_filter.append(
                'subnet:%s' % (ip_subnet)
            )

        if len(ip_address) > 0:
            system_info = True
            node_filter.append(
                'ip:%s' % (ip_address)
            )

        interfaces_summary_info = False
        if 'intf' in view:
            interfaces_summary_info = True
            if node_role == 'any':
                node_filter.append(
                    'role:!controller'
                )

        if 'power' in view:
            power_info = True

        if 'psu' in view:
            psu_info = True

        if 'sensor' in view:
            sensor_info = True

        if 'ip' in view:
            system_info = True

        if 'temp' in view:
            temp_info = True

        nodes = []

        for apic_handler in apic_handlers:
            apic_nodes = apic_handler['handler'].get_nodes(
                node_filter=node_filter,
                interfaces_summary_info=interfaces_summary_info,
                power_info=power_info,
                psu_info=psu_info,
                sensor_info=sensor_info,
                system_info=system_info,
                temp_info=temp_info
            )
            if apic_nodes is None:
                continue

            nodes = nodes + apic_nodes

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    nodes,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(nodes)

        if 'state' in view:
            aci_output_handler.print_nodes(
                nodes,
                title=True
            )

        if 'intf' in view:
            aci_output_handler.print_nodes_intf(
                nodes,
                title=True
            )

        if 'ip' in view:
            aci_output_handler.print_nodes_system(
                nodes,
                title=True
            )

        if 'power' in view:
            aci_output_handler.print_nodes_power(
                nodes,
                title=True
            )

        if 'psu' in view:
            aci_output_handler.print_nodes_psu(
                nodes,
                title=True
            )

        if 'sensor' in view:
            aci_output_handler.print_nodes_sensor(
                nodes,
                title=True
            )

        if 'temp' in view:
            aci_output_handler.print_nodes_temp(
                nodes,
                title=True
            )

        ctx.my_output.default('Filter: pod, role, id, name, model, address, subnet', before_newline=True)
        ctx.my_output.default('View:   state (def), intf, ip, power, psu, sensor, temp, all')

        if len(nodes) == 0:
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
