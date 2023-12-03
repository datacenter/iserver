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


@click.command("srnns")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--node", "node_name", default='', callback=validations.empty_string_to_none, help="Filter by node name")
@click.option("--intf", "interface_name", default='', callback=validations.empty_string_to_none, help="Filter by interface name")
@click.option("--view", "-v", default=['state'], help="[state|policy|vf|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_srnns_command(
        ctx,
        cluster,
        node_name,
        interface_name,
        view,
        output,
        devel
        ):
    """Get k8s sriov network node state"""

    # iserver get k8s srnns

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|policy|vf|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, cluster_type='ocp')
        if k8s_handlers is None:
            raise ErrorExit

        object_filter = []
        if node_name is not None:
            object_filter.append(
                'name:%s' % (node_name)
            )

        if interface_name is not None:
            object_filter.append(
                'interface:%s' % (interface_name)
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
            sriov_network_node_states = k8s_handlers.get_sriov_network_node_states(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    sriov_network_node_states,
                    indent=4
                )
            )
            return

        sriov_network_node_states = k8s_handlers.get_sriov_network_node_states(
            object_filter=object_filter
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    sriov_network_node_states,
                    indent=4
                )
            )
            return

        if 'state' in view:
            k8s_output_handler.print_sriov_network_nodes_state(
                sriov_network_node_states,
                title=True
            )

        if 'policy' in view:
            k8s_output_handler.print_sriov_network_nodes_state_policy(
                sriov_network_node_states,
                title=True
            )

        if 'vf' in view:
            k8s_output_handler.print_sriov_network_nodes_state_vf(
                sriov_network_node_states,
                title=True
            )

        ctx.my_output.default('Filter: node, intf', before_newline=True)
        ctx.my_output.default('View:   state (def), policy, vf, all')

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
