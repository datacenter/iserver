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


@click.command("bgp")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--asn", "bgp_asn", default='', callback=validations.empty_string_to_none, help="Filter by BGP ASN")
@click.option("--vrf", "bgp_vrf", default='', callback=validations.empty_string_to_none, help="Filter by VRF name")
@click.option("--rtr-ip", "rtr_ip_address", default='', callback=validations.validate_ip, help="Filter by BGP Router IP address")
@click.option("--rtr-subnet", "rtr_ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by BGP Router IP subnet")
@click.option("--type", "nbr_type", type=click.Choice(['any', 'ibgp', 'ebgp'], case_sensitive=False), default='any', show_default=True, help="Filter by BGP neighbor type")
@click.option("--nbr-ip", "nbr_ip_address", default='', callback=validations.validate_ip, help="Filter by BPG Neighbor IP address")
@click.option("--nbr-subnet", "nbr_ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by BPG Neighbor IP subnet")
@click.option("--state", "nbr_state", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True, help="Filter by BGP neighbor state")
@click.option("--intf", "source_interface", default='', callback=validations.empty_string_to_none, help="Filter by BGP Neighbor source interface")
@click.option("--view", "-v", type=click.Choice(['default', 'node', 'vrf', 'trans', 'conn', 'af', 'verbose', 'route'], case_sensitive=False), multiple=True, show_default=False)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_bgp_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        bgp_asn,
        bgp_vrf,
        rtr_ip_address,
        rtr_ip_subnet,
        nbr_type,
        nbr_ip_address,
        nbr_ip_subnet,
        nbr_state,
        source_interface,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol bgp"""

    # iserver get aci node proto bgp

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
            pod_id=pod_id
        )
        if nodes_info is None:
            raise ErrorExit

        bgp_filter = []
        if bgp_asn is not None:
            bgp_filter.append(
                'asn:%s' % (bgp_asn)
            )

        if bgp_vrf is not None:
            bgp_filter.append(
                'vrf:%s' % (bgp_vrf)
            )

        if len(rtr_ip_address) > 0:
            bgp_filter.append(
                'rtr-ip:%s' % (rtr_ip_address)
            )

        if len(rtr_ip_subnet) > 0:
            bgp_filter.append(
                'rtr-subnet:%s' % (rtr_ip_subnet)
            )

        if len(nbr_type) > 0:
            bgp_filter.append(
                'nbr-type:%s' % (nbr_type)
            )

        if len(nbr_ip_address) > 0:
            bgp_filter.append(
                'nbr-ip:%s' % (nbr_ip_address)
            )

        if len(nbr_ip_subnet) > 0:
            bgp_filter.append(
                'nbr-subnet:%s' % (nbr_ip_subnet)
            )

        if nbr_state is not None:
            bgp_filter.append(
                'state:%s' % (nbr_state)
            )

        if source_interface is not None:
            bgp_filter.append(
                'interface:%s' % (source_interface)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        instances = []
        domains = []
        neighbors = []
        routes = []

        stats_info = False
        prefix_info = False
        if 'verbose' in view:
            stats_info = True
            prefix_info = True

        if 'route' in view:
            stats_info = True
            prefix_info = True

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_bgp(
                node_info['podId'],
                node_info['id'],
                bgp_filter=bgp_filter,
                stats_info=stats_info,
                prefix_info=prefix_info
            )

            if proto_info is None:
                continue

            instances.append(
                proto_info
            )
            domains = domains + proto_info['domains']
            neighbors = neighbors + proto_info['neighbors']
            if prefix_info:
                for neighbor_info in proto_info['neighbors']:
                    routes = routes + neighbor_info['routes']

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

        if 'node' in view:
            ctx.my_output.json_output(
                instances
            )

            aci_output_handler.print_proto_bgp_instances(
                instances
            )

        if 'vrf' in view:
            ctx.my_output.json_output(
                domains
            )

            aci_output_handler.print_proto_bgp_domains(
                domains
            )

        if 'default' in view:
            ctx.my_output.json_output(
                neighbors
            )

            aci_output_handler.print_proto_bgp_neighbors_summary(
                neighbors
            )

        if 'trans' in view:
            ctx.my_output.json_output(
                neighbors
            )

            aci_output_handler.print_proto_bgp_neighbors_transport(
                neighbors
            )

        if 'conn' in view:
            ctx.my_output.json_output(
                neighbors
            )

            aci_output_handler.print_proto_bgp_neighbors_connections(
                neighbors
            )

        if 'af' in view:
            ctx.my_output.json_output(
                neighbors
            )

            aci_output_handler.print_proto_bgp_neighbors_af(
                neighbors
            )

        if 'verbose' in view:
            ctx.my_output.json_output(
                neighbors
            )

            for neighbor in neighbors:
                aci_output_handler.print_proto_bgp_neighbors_summary(
                    [neighbor]
                )

                aci_output_handler.print_proto_bgp_neighbor(
                    neighbor
                )

        if 'route' in view:
            aci_output_handler.print_protocol_ipv4_routes(
                routes
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
