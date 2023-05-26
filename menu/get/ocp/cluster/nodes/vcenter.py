import sys
import json
import traceback
import threading
import click

from menu import progress
from menu import validations

from lib.ocp.state import vcenter as ocp_vcenter


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vcenter")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name, type=click.STRING, help="Cluster Name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_cluster_nodes_vcenter_command(ctx, cluster_name, output, devel):
    """Get ocp cluster nodes vcenter"""

    # iserver get ocp cluster nodes vcenter

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        ocp_vcenter_handler = ocp_vcenter.OcpVcenter(
            log_id=ctx.run_id
        )

        info = ocp_vcenter_handler.get_ocp_cluster_vcenter(cluster_name)
        if info is None:
            ctx.busy = False
            ctx.my_output.error('Failed to get OCP cluster vcenter state')
            raise ErrorExit

        if output == 'json':
            ctx.busy = False
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    info,
                    indent=4
                )
            )
            return

        ctx.busy = False
        ctx.my_output.json_output(info)

        ocp_vcenter_handler.print_ocp_cluster_vcenter(info)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
