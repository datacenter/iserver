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
@click.option("--xd", "xd_filter", default='', callback=validations.validate_aci_xd, help="Cross domain filter")
@click.option("--view", "-v", type=click.Choice(['summary', 'stats', 'nei', 'verbose'], case_sensitive=False), default='nei', show_default=True)
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
        xd_filter,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol lldp"""

    # iserver get aci node proto lldp

    ctx.developer = devel
    ctx.output = output

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

        xd_mac, xd_interface = validations.resolve_aci_xd(
            ctx,
            xd_filter,
            output
        )
        if xd_mac is not None:
            for item in xd_mac:
                adjacency_filter.append(
                    'mac:%s' % (item)
                )

        if device is not None:
            adjacency_filter.append(
                'device:%s' % (device)
            )

        if mac is not None:
            adjacency_filter.append(
                'mac:%s' % (mac)
            )

        instance_info = False
        stats_info = False
        adjacency_info = False

        if view in ['summary', 'verbose']:
            instance_info = True
            stats_info = True
            adjacency_info = True

        if view in ['stats', 'verbose']:
            stats_info = True

        if view in ['nei', 'verbose']:
            adjacency_info = True

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        instance = []
        stats = []
        adjacency = []

        for node_info in nodes_info:
            protocol_lldp_info = apic_handler.get_protocol_lldp(
                node_info['podId'],
                node_info['id'],
                adjacency_filter=adjacency_filter,
                instance_info=instance_info,
                stats_info=stats_info,
                adjacency_info=adjacency_info
            )

            if protocol_lldp_info is None:
                continue

            if instance_info and protocol_lldp_info['instance'] is not None:
                instance.append(
                    protocol_lldp_info['instance']
                )

            if stats_info and protocol_lldp_info['stats'] is not None:
                stats.append(
                    protocol_lldp_info['stats']
                )

            if adjacency_info and protocol_lldp_info['adjacency'] is not None:
                adjacency = adjacency + protocol_lldp_info['adjacency']
                lldp_context = apic_handler.add_protocol_lldp_adjacency_context(
                    lldp_context,
                    adjacency
                )

        ctx.busy = False

        if len(instance) == 0 and len(stats) == 0 and len(adjacency) == 0:
            raise NoResultExit

        result = {}
        result['instance'] = instance
        result['stats'] = stats
        result['adjacency'] = adjacency

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    result,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(result)

        if view in ['summary', 'verbose']:
            aci_output_handler.print_proto_lldp_instance(
                instance
            )

        if view in ['stats', 'verbose']:
            aci_output_handler.print_proto_lldp_instances_stats(
                stats
            )

        if view in ['nei', 'verbose']:
            aci_output_handler.print_lldp_adjacency_endpoints(
                adjacency
            )

            if xd_interface is not None:
                aci_output_handler.print_lldp_adjacency_interface_endpoints(
                    adjacency,
                    xd_interface
                )

        if context_handler.is_interface_defined(lldp_context):
            success = context_handler.set(
                'lldp',
                lldp_context
            )
            if success:
                ctx.my_output.default('Interface context: lldp')

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
