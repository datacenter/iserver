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


@click.command("srnnp")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--resource", default='', callback=validations.empty_string_to_none, help="Filter by resource")
@click.option("--type", "device_type", type=click.Choice(['vfio', 'net', 'any'], case_sensitive=False), default='any', help="Device type")
@click.option("--view", "-v", default=['state'], help="[state|srn|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_srnnp_command(
        ctx,
        cluster,
        name,
        resource,
        device_type,
        view,
        output,
        devel
        ):
    """Get k8s sriov network node policy"""

    # iserver get k8s srnnp

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|srn|all',
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

        sriov_network_info = True

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if resource is not None:
            object_filter.append(
                'resource:%s' % (resource)
            )

        if device_type != 'any':
            object_filter.append(
                'device_type:%s*' % (device_type)
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
            sriov_network_node_policies = k8s_handlers.get_sriov_network_node_policies(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    sriov_network_node_policies,
                    indent=4
                )
            )
            return

        sriov_network_node_policies = k8s_handlers.get_sriov_network_node_policies(
            object_filter=object_filter,
            sriov_network_info=sriov_network_info
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    sriov_network_node_policies,
                    indent=4
                )
            )
            return

        if 'state' in view:
            k8s_output_handler.print_sriov_network_node_policies(
                sriov_network_node_policies,
                title=True
            )

        if 'srn' in view:
            k8s_output_handler.print_sriov_network_node_policies_srn(
                sriov_network_node_policies,
                title=True
            )

        ctx.my_output.default('Filter: name, resource, type', before_newline=True)
        ctx.my_output.default('View:   state (def), srn, all')

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
