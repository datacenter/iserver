import sys
import json
import threading
import traceback
import click

from lib.aci import output as aci_output
from lib import context

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("lldp")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--device", default='', callback=validations.empty_string_to_none, help="Filter neighbor by device name")
@click.option("--mac", default='', callback=validations.empty_string_to_none, help="Filter neighbor by mac address")
@click.option("--xd", "xd_filter", default='', callback=validations.validate_aci_xd, help="Cross domain filter")
@click.option("--output", "-o", type=click.Choice(['instance', 'nei', 'stats', 'verbose', 'json'], case_sensitive=False), default='instance', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_lldp_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        device,
        mac,
        xd_filter,
        output,
        devel
        ):
    """Get aci node protocol lldp"""

    # iserver get aci node proto lldp

    ctx.developer = devel
    if output == 'json':
        ctx.output = 'json'
    else:
        ctx.output = 'default'

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_username,
            controller_password,
            show_selected=False
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

        xd_filter = validations.resolve_aci_xd(
            ctx,
            xd_filter,
            output
        )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        instances = []
        adjacency = []
        lldp_context = {}
        lldp_context['apic'] = [controller['name']]
        lldp_context['node'] = {}
        lldp_context['node'][controller['name']] = []
        lldp_context['interface'] = {}
        lldp_context['interface'][controller['name']] = []

        lldp_filter = []

        if output in ['nei', 'verbose', 'json']:
            if xd_filter is not None:
                for mac_filter in xd_filter['mac']:
                    lldp_filter.append(
                        'mac:%s' % (mac_filter)
                    )

            if device is not None:
                lldp_filter.append(
                    'device:%s' % (device)
                )

            if mac is not None:
                lldp_filter.append(
                    'mac:%s' % (mac)
                )

        for node_info in nodes_info:
            node_instance_info = apic_handler.get_protocol_lldp(
                node_info['podId'],
                node_info['id'],
                lldp_filter=lldp_filter
            )

            instances.append(
                node_instance_info
            )
            adjacency = adjacency + node_instance_info['adjacency']

            for item in node_instance_info['adjacency']:
                node_name = apic_handler.get_node_name(item['node_id'].split('-')[1])
                if node_name not in lldp_context['node'][controller['name']]:
                    lldp_context['node'][controller['name']].append(
                        node_name
                    )

                interface_name = '%s:%s:%s' % (
                    item['pod_id'],
                    item['node_id'],
                    item['interface_id']
                )
                if interface_name not in lldp_context['interface'][controller['name']]:
                    lldp_context['interface'][controller['name']].append(
                        interface_name
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

        if output == 'instance':
            aci_output_handler.print_proto_lldp_instances(
                instances
            )

        if output == 'stats':
            aci_output_handler.print_proto_lldp_instances_stats(
                instances
            )

        if output == 'nei':
            aci_output_handler.print_lldp_adjacency_endpoints(
                adjacency
            )

            if len(lldp_context['interface'][controller['name']]) > 0:
                context_handler = context.Context(log_id=ctx.run_id)
                success = context_handler.set(
                    'lldp',
                    lldp_context
                )
                if not success:
                    ctx.my_output.error('Failed to set interface context')
                else:
                    ctx.my_output.default('Interface context: lldp')

        if output == 'verbose':
            for instance in instances:
                aci_output_handler.print_proto_lldp(
                    instance
                )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
