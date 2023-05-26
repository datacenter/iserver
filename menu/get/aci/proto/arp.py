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


@click.command("arp")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--vrf", "vrf_name", default='', callback=validations.empty_string_to_none, help="Filter by VRF name")
@click.option("--mac", "mac_address", default='', callback=validations.empty_string_to_none, help="Filter by MAC address")
@click.option("--ip", "ip_address", default='', callback=validations.validate_ip, help="Filter by IP")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by subnet")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'verbose'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_arp_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        vrf_name,
        mac_address,
        ip_address,
        ip_subnet,
        output,
        devel
        ):
    """Get aci node protocol arp"""

    # iserver get aci node proto arp

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
            controller_password
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

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        arp_domain_filter = []
        if vrf_name is not None:
            arp_domain_filter.append(
                'name:%s' % (vrf_name)
            )

        if mac_address is not None:
            arp_domain_filter.append(
                'mac:%s' % (mac_address)
            )

        if len(ip_address) > 0:
            arp_domain_filter.append(
                'ip:%s' % (ip_address)
            )

        if len(ip_subnet) > 0:
            arp_domain_filter.append(
                'subnet:%s' % (ip_subnet)
            )

        instances = []
        adjacency = []

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_arp(
                node_info['podId'],
                node_info['id'],
                arp_domain_filter=arp_domain_filter,
                adjacency_info=True,
                interface_info=True
            )

            adjacency = adjacency + proto_info['adjacency']
            instances.append(
                proto_info
            )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    proto_info,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(proto_info)

        if output == 'default':
            aci_output_handler.print_protocol_arp_adjacencies(
                adjacency
            )

        if output == 'verbose':
            for instance in instances:
                aci_output_handler.print_protocol_arp(
                    instance
                )

        ctx.busy = False

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
