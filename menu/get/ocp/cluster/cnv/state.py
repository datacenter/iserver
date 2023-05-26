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


@click.command("state")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Cluster Name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_cluster_cnv_state_command(ctx, cluster_name, output, devel):
    """Get ocp cluster cnv state"""

    # iserver get ocp cluster cnv state

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name
        )
        if ocp_handler is None:
            raise ErrorExit

        if not ocp_handler.is_connected():
            ctx.busy = False
            ctx.my_output.error(
                'OCP connection failed'
            )
            raise ErrorExit

        cnv = ocp_handler.get_ocp_cnv_state()
        nodes = ocp_handler.get_ocp_nodes_info()

        info = {}
        info['cnv'] = cnv
        info['nodes'] = nodes

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    info,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(info)
        ocp_handler.print_ocp_cnv_state(cnv)
        ocp_handler.print_ocp_nodes_list(nodes)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
