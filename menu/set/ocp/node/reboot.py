import sys
import traceback
import click

from lib.workflow.ocp_node import reboot

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("reboot")
@click.pass_obj
@click.option("--cluster", "cluster_name", callback=validations.empty_string_to_none, help="OCP cluster name")
@click.option("--node", multiple=True, help="Node name")
def set_ocp_node_reboot_command(
        ctx,
        cluster_name,
        node
        ):
    """Set k8s node reboot"""

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['node'] = node
        success = reboot.run(
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
