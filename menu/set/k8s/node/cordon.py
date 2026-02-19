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


@click.command("cordon")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--node", default='', callback=validations.empty_string_to_none, help="Node name")
def set_k8s_node_cordon_command(
        ctx,
        cluster,
        node,
        ):
    """Set k8s node cordon"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handler = validations.validate_kubernetes_name(ctx, cluster, log_id=ctx.run_id)
        if k8s_handler is None:
            raise ErrorExit

        if k8s_handler.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit

        success = k8s_handler.set_node_cordon(node, ctx.my_output)
        if not success:
            raise ErrorExit
        
        k8s_nodes = k8s_handler.get_nodes(object_filter=['name:%s' % (node)], cache_enabled=False)
        k8s_output_handler.print_nodes_state(k8s_nodes)

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
