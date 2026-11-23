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


@click.command("node")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--label", default='', callback=validations.empty_string_to_none, help="Filter by label")
@click.option("--view", "-v", default=['state'], help="[state|ver|cap|label|sriov|sriov-phy|sriov-policy|sriov-network|sriov-vf|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_node_command(
        ctx,
        cluster,
        name,
        label,
        view,
        output,
        devel
        ):
    """Get k8s node"""

    # iserver get k8s node

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|ver|cap|label|sriov|sriov-phy|sriov-policy|sriov-network|sriov-vf|all',
        'state',
        [
            'sriov:sriov-phy,sriov-policy,sriov-network,sriov-vf'
        ]
    )
    if view is None:
        sys.exit(1)

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if label is not None:
            object_filter.append(
                'label:%s' % (label)
            )

        ocp_handler = None
        for item in view:
            if 'sriov' in item:
                try:
                    ocp_handler = validations.validate_ocp_cluster(
                        ctx,
                        cluster
                    )
                except BaseException:
                    ocp_handler = None

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
            nodes = k8s_handlers.get_nodes(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    nodes,
                    indent=4
                )
            )
            return

        k8s_nodes = k8s_handlers.get_nodes(
            object_filter=object_filter
        )

        if ocp_handler is not None:
            sriov_phy_info = False
            sriov_policy_info = False
            sriov_network_info = False
            sriov_vf_info = False

            if view == 'sriov-phy':
                sriov_phy_info = True

            if view == 'sriov-policy':
                sriov_policy_info = True

            if view == 'sriov-network':
                sriov_network_info = True

            if view == 'sriov-vf':
                sriov_vf_info = True

            ocp_nodes = ocp_handler.get_ocp_nodes(
                node_filter=object_filter,
                sriov_phy_info=sriov_phy_info,
                sriov_policy_info=sriov_policy_info,
                sriov_network_info=sriov_network_info,
                sriov_vf_info=sriov_vf_info
            )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    k8s_nodes,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(k8s_nodes)

        if 'state' in view:
            k8s_output_handler.print_nodes_state(
                k8s_nodes
            )

        if 'ver' in view:
            k8s_output_handler.print_nodes_version(
                k8s_nodes,
                title=True
            )

        if 'cap' in view:
            k8s_output_handler.print_nodes_capacity(
                k8s_nodes,
                title=True
            )

        if 'label' in view:
            k8s_output_handler.print_nodes_label(
                k8s_nodes,
                title=True
            )

        if 'sriov-phy' in view:
            if ocp_handler is not None:
                k8s_output_handler.print_ocp_nodes_sriov_phy(
                    ocp_nodes,
                    title=True
                )

        if 'sriov-policy' in view:
            if ocp_handler is not None:
                k8s_output_handler.print_ocp_nodes_sriov_policy(
                    ocp_nodes,
                    title=True
                )

        if 'sriov-network' in view:
            if ocp_handler is not None:
                k8s_output_handler.print_ocp_nodes_sriov_network(
                    ocp_nodes,
                    title=True
                )

        if 'sriov-vf' in view:
            if ocp_handler is not None:
                k8s_output_handler.print_ocp_nodes_sriov_vf(
                    ocp_nodes,
                    title=True
                )

        ctx.my_output.default('Filter: name, label', before_newline=True)
        ctx.my_output.default('View:   state (def), ver, cap, label, sriov, sriov-phy, sriov-policy, sriov-network, sriov-vf, all')

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
