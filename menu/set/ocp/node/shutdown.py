import sys
import traceback
import click

from lib.workflow.ocp_node import shutdown

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("shutdown")
@click.pass_obj
@click.option("--cluster", "cluster_name", callback=validations.empty_string_to_none, help="OCP cluster name")
@click.option("--node", multiple=True, help="Node name")
@click.option("--no-checks", is_flag=True, show_default=True, default=False, help="Skip checks")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode in case of eviction problems")
def set_ocp_node_shutdown_command(
        ctx,
        cluster_name,
        node,
        no_checks,
        no_confirm
        ):
    """Set k8s node graceful shutdown"""

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['node'] = []
        for item in node:
            params['node'].append(item)
        params['checks'] = not no_checks
        params['confirmation'] = not no_confirm
        success = shutdown.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
