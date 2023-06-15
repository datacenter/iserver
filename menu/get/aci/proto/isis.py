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


@click.command("isis")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--domain", "domain_name", default='', callback=validations.empty_string_to_none, help="Filter by domain name")
@click.option("--view", "-v", type=click.Choice(['default', 'intf', 'lsp', 'neighbor', 'route', 'tree', 'tunnel', 'verbose'], case_sensitive=False), multiple=True, show_default=False)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_isis_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        domain_name,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol isis"""

    # iserver get aci node proto isis

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

        isis_domain_filter = []
        if domain_name is not None:
            isis_domain_filter.append(
                'name:%s' % (domain_name)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        instances = []
        domains = []

        intf = []
        lsp = []
        neighbor = []
        route = []
        tree = []
        tunnels = []

        intf_info = False
        lsp_info = False
        neighbor_info = False
        route_info = False
        tree_info = False
        tunnel_info = False

        if 'verbose' in view:
            intf_info = True
            lsp_info = True
            neighbor_info = True
            route_info = True
            tree_info = True
            tunnel_info = True

        if 'intf' in view:
            intf_info = True

        if 'lsp' in view:
            lsp_info = True

        if 'neighbor' in view:
            neighbor_info = True

        if 'route' in view:
            route_info = True

        if 'tree' in view:
            tree_info = True

        if 'tunnel' in view:
            tunnel_info = True

        for node_info in nodes_info:
            node_instance_info = apic_handler.get_protocol_isis(
                node_info['podId'],
                node_info['id'],
                isis_domain_filter=isis_domain_filter,
                interface_info=intf_info,
                lsp_info=lsp_info,
                neighbor_info=neighbor_info,
                route_info=route_info,
                tree_info=tree_info,
                tunnel_info=tunnel_info
            )

            if node_instance_info is None:
                continue

            instances.append(
                node_instance_info
            )
            domains = domains + node_instance_info['domain']

            if intf_info:
                for domain_info in node_instance_info['domain']:
                    intf = intf + domain_info['interface']

            if lsp_info:
                for domain_info in node_instance_info['domain']:
                    lsp = lsp + domain_info['lsp']

            if neighbor_info:
                for domain_info in node_instance_info['domain']:
                    neighbor = neighbor + domain_info['neighbor']

            if route_info:
                for domain_info in node_instance_info['domain']:
                    route = route + domain_info['route']

            if tree_info:
                for domain_info in node_instance_info['domain']:
                    tree = tree + domain_info['tree']

            if tunnel_info:
                for domain_info in node_instance_info['domain']:
                    tunnels = tunnels + domain_info['tunnel']

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

        if 'default' in view:
            ctx.my_output.json_output(instances)
            aci_output_handler.print_proto_isis_instances(
                instances
            )

        if 'intf' in view:
            ctx.my_output.json_output(intf)
            aci_output_handler.print_proto_isis_interfaces(
                intf
            )

        if 'lsp' in view:
            ctx.my_output.json_output(lsp)
            aci_output_handler.print_proto_isis_lsps(
                lsp
            )

        if 'neighbor' in view:
            ctx.my_output.json_output(neighbor)
            aci_output_handler.print_proto_isis_neighbors(
                neighbor
            )

        if 'route' in view:
            ctx.my_output.json_output(route)
            aci_output_handler.print_proto_isis_routes(
                route
            )

        if 'tree' in view:
            ctx.my_output.json_output(tree)
            aci_output_handler.print_proto_isis_trees(
                tree
            )

        if 'tunnel' in view:
            ctx.my_output.json_output(tunnels)
            aci_output_handler.print_proto_isis_tunnels(
                tunnels,
                title=True
            )

        if 'verbose' in view:
            ctx.my_output.json_output(instances)
            for instance in instances:
                aci_output_handler.print_proto_isis(
                    instance
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
