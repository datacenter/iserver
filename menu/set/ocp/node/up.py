import sys
import json
import threading
import traceback
import click

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("up")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', help="OCP cluster name")
@click.option("--node", "node_name", default='', help="OCP cluster node name")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="No wait")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_ocp_node_up(
        ctx,
        cluster_name,
        node_name,
        no_wait,
        verbose,
        debug,
        devel
        ):
    """Set ocp cluster node up"""

    # iserver set ocp node up

    ctx.developer = devel

    try:
        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name,
            verbose=verbose,
            debug=debug
        )
        if ocp_handler is None:
            raise ErrorExit

        if not validations.validate_ocp_node(ctx, ocp_handler, node_name):
            raise ErrorExit

        if not ocp_handler.set_ocp_node_up(node_name, wait=not no_wait):
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
