import sys
import traceback
import click

from lib.workflow.ocp_node import reload

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("reload")
@click.pass_obj
@click.option("--cluster", "cluster_name", callback=validations.empty_string_to_none, help="OCP cluster name")
@click.option("--node", multiple=True, help="Node name")
@click.option("--no-pre", is_flag=True, show_default=True, default=False, help="Skip pre checks")
@click.option("--no-post", is_flag=True, show_default=True, default=False, help="Skip post checks")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode in case of eviction problems")
def set_ocp_node_reload_command(
        ctx,
        cluster_name,
        node,
        no_pre,
        no_post,
        no_confirm
        ):
    """Set k8s node graceful reboot (reload)"""

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['node'] = node
        params['pre'] = not no_pre
        params['post'] = not no_post
        params['confirmation'] = not no_confirm
        success = reload.run(
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
