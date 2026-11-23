import sys
import json
import threading
import traceback
import click

from lib.k8s import main as k8s
from lib.k8s import settings as k8s_settings
from lib.k8s import output as k8s_output

from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("kc")
@click.pass_obj
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify api access")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_kc_command(
        ctx,
        verify,
        output,
        devel
        ):
    """Get k8s kubeconfig"""

    # iserver get k8s kc

    ctx.developer = devel
    ctx.output = output

    try:
        k8s_settings_handler = k8s_settings.K8sSettings(log_id=ctx.run_id)
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)

        clusters_info = k8s_settings_handler.get_clusters_kubeconfig_info()

        if clusters_info is None or len(clusters_info) == 0:
            ctx.my_output.default('No kubernetes clusters defined')
            return

        if verify:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

            for cluster_info in clusters_info:
                k8s_handler = k8s.K8s(cluster_info['kubeconfigFilename'])
                if k8s_handler.get_api() is not None:
                    cluster_info['kubeApi'] = True
                    cluster_info['kubeApiTick'] = '\u2713'
                    cluster_info['__Output']['kubeApiTick'] = 'Green'
                else:
                    cluster_info['kubeApi'] = False
                    cluster_info['kubeApiTick'] = '\u2717'
                    cluster_info['__Output']['kubeApiTick'] = 'Red'

            ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    clusters_info,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(clusters_info)

        k8s_output_handler.print_clusters_kubeconfig(
            clusters_info,
            title=True
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
