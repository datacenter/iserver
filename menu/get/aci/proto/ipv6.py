import sys
import json
import traceback
import copy
import threading
import click

from lib.aci import output as aci_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ipv6")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--vrf", "vrf_name", default='', callback=validations.empty_string_to_none, help="VRF")
@click.option("--type", "route_filter", type=click.Choice(['ibgp', 'ebgp', 'bgp', 'static', 'local', 'direct'], case_sensitive=False), multiple=True)
@click.option("--ip", "ip_address_filter", default='', callback=validations.validate_ip, help="IP Address filter")
@click.option("--subnet", "ip_subnet_filter", default='', callback=validations.validate_ip_subnet, help="IP Subnet filter")
@click.option("--longer", "longer_prefixes", is_flag=True, show_default=True, default=False, help="Match longer prefixes")
@click.option("--output", "-o", type=click.Choice(['route', 'summary', 'json'], case_sensitive=False), default='route', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_ipv6_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        vrf_name,
        route_filter,
        ip_address_filter,
        ip_subnet_filter,
        longer_prefixes,
        output,
        devel
        ):
    """Get aci node protocol ipv6"""

    # iserver get aci node proto ipv6

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

        ipv6_filter = []
        if vrf_name is not None:
            ipv6_filter.append(
                'vrf:%s' % (vrf_name)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        domains_info = []
        routes_info = []

        for node_info in nodes_info:
            if output in ['summary', 'json']:
                node_domains_info = copy.deepcopy(
                    apic_handler.get_protocol_ipv6_domains(
                        node_info['podId'],
                        node_info['id'],
                        routes_info=True,
                        ipv6_domain_filter=ipv6_filter
                    )
                )
            else:
                node_domains_info = copy.deepcopy(
                    apic_handler.get_protocol_ipv6_domains(
                        node_info['podId'],
                        node_info['id'],
                        routes_info=False,
                        ipv6_domain_filter=ipv6_filter
                    )
                )

            domains_info = domains_info + node_domains_info

            if output in ['route', 'json']:
                if ip_address_filter is not None and len(ip_address_filter) > 0:
                    route_filter = route_filter + ('ip:%s' % (ip_address_filter), )

                if ip_subnet_filter is not None and len(ip_subnet_filter) > 0:
                    if longer_prefixes:
                        route_filter = route_filter + ('subnet-longer:%s' % (ip_subnet_filter), )
                    else:
                        route_filter = route_filter + ('subnet:%s' % (ip_subnet_filter), )

                node_routes_info = []
                for domain_info in node_domains_info:
                    info = copy.deepcopy(
                        apic_handler.get_protocol_ipv6_routes(
                            node_info['podId'],
                            node_info['id'],
                            ipv6_domain_name=domain_info['name'],
                            route_filter=route_filter
                        )
                    )
                    node_routes_info = node_routes_info + info

                routes_info = routes_info + node_routes_info

        ctx.busy = False

        if output == 'json':
            info = {}
            info['summary'] = domains_info
            info['route'] = routes_info

            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    info,
                    indent=6
                )
            )
            return

        if output == 'summary':
            ctx.my_output.json_output(domains_info)
            aci_output_handler.print_protocol_ipv6_domains(
                domains_info
            )

        if output == 'route':
            ctx.my_output.json_output(routes_info)
            aci_output_handler.print_protocol_ipv6_routes(
                routes_info
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
