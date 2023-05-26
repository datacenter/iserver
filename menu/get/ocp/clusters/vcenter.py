import sys
import json
import traceback
import threading
import click

from menu import progress

from lib.ocp.state.vcenter import main as ocp_vcenter


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vcenter")
@click.pass_obj
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_clusters_vcenter_command(ctx, output, devel):
    """Get ocp clusters vcenter"""

    # iserver get ocp clusters vcenter

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        ocp_vcenter_handler = ocp_vcenter.OcpVcenter(
            log_id=ctx.run_id
        )

        clusters = ocp_vcenter_handler.get_ocp_clusters_vcenter()
        if clusters is None:
            ctx.busy = False
            ctx.my_output.error('Failed to get OCP clusters vcenter state')
            raise ErrorExit

        if output == 'json':
            ctx.busy = False
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    clusters,
                    indent=4
                )
            )
            return

        ctx.busy = False
        ctx.my_output.json_output(clusters)

        ocp_vcenter_handler.print_ocp_clusters_vcenter(clusters)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
