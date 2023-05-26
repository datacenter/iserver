import sys
import json
import traceback
import threading
import click

from menu import progress
from menu import validations

from lib.ocp.state import kubeconfig as ocp_kubeconfig


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("kc")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name, type=click.STRING, help="Cluster Name")
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify SSH access")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_cluster_kc_command(ctx, cluster_name, verify, output, devel):
    """Get ocp clusters kubeconfig"""

    # iserver get ocp clusters kc

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        ocp_kubeconfig_handler = ocp_kubeconfig.OcpKubeconfig(
            log_id=ctx.run_id
        )

        clusters = ocp_kubeconfig_handler.get_ocp_cluster_kubeconfig(
            cluster_name,
            validate=verify
        )
        if clusters is None:
            ctx.busy = False
            ctx.my_output.error('Failed to get OCP cluster kubeconfig')
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

        ocp_kubeconfig_handler.print_ocp_cluster_kubeconfig(
            clusters,
            validated=verify
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
