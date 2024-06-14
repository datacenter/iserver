import sys
import traceback
import click

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("nestedhv")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', help="OCP cluster name")
@click.option("--node", "node_name", default='', help="OCP cluster node name")
@click.option("--disabled", is_flag=True, show_default=True, default=False, help="Disable nested hv")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_ocp_node_nestedhv(
        ctx,
        cluster_name,
        node_name,
        disabled,
        verbose,
        debug,
        devel
        ):
    """Set ocp cluster node nestedhv"""

    # iserver set ocp node nestedhv

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

        if not ocp_handler.set_ocp_node_nestedhv(node_name, enabled=not disabled):
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
