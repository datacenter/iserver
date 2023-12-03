import sys
import json
import threading
import traceback
import click

from lib.k8s import output as k8s_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("nns")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Include verbose")
@click.option("--view", "-v", default=['all'], help="[dns|route|bond|eth|lb|ovs|vf|vlan|intf|route|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_nns_command(
        ctx,
        cluster,
        name,
        verbose,
        view,
        output,
        devel
        ):
    """Get k8s node network state"""

    # iserver get k8s nncp

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'dns|route|bond|eth|lb|ovs|vf|vlan|intf|route|all',
        'all',
        [
            'intf:bond,eth,lb,ovs,vf,vlan'
        ]
    )
    if view is None:
        sys.exit(1)

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, cluster_type='ocp')
        if k8s_handlers is None:
            raise ErrorExit

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if output not in ['json', 'mo']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if k8s_handlers.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit

        if output == 'mo':
            states = k8s_handlers.get_node_network_states(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    states,
                    indent=4
                )
            )
            return

        states = k8s_handlers.get_node_network_states(
            object_filter=object_filter
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    states,
                    indent=4
                )
            )
            return

        if 'dns' in view:
            k8s_output_handler.print_node_network_state_dns(
                states,
                title=True
            )

        if 'route' in view:
            k8s_output_handler.print_node_network_state_route(
                states,
                title=True
            )

        if 'bond' in view:
            k8s_output_handler.print_node_network_state_bond(
                states,
                ethtool=verbose,
                options=verbose,
                title=True
            )

        if 'eth' in view:
            k8s_output_handler.print_node_network_state_ethernet(
                states,
                ethtool=verbose,
                title=True
            )

        if 'vf' in view:
            k8s_output_handler.print_node_network_state_vf(
                states,
                ethtool=verbose,
                title=True
            )

        if 'vlan' in view:
            k8s_output_handler.print_node_network_state_vlan(
                states,
                ethtool=verbose,
                title=True
            )

        if 'lb' in view:
            k8s_output_handler.print_node_network_state_lb(
                states,
                ethtool=verbose,
                options=verbose,
                title=True
            )

            k8s_output_handler.print_node_network_state_lb_interfaces(
                states
            )

        if 'ovs' in view:
            k8s_output_handler.print_node_network_state_ovs(
                states,
                ethtool=verbose,
                title=True
            )

            k8s_output_handler.print_node_network_state_ovs_interfaces(
                states,
                ethtool=verbose
            )

        ctx.my_output.default('Filter: name', before_newline=True)
        ctx.my_output.default('View:   all (def), dns, route, intf, bond, eth, vlan, vf, lb, ovs')

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
