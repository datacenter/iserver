import sys
import json
import threading
import traceback
import click

from lib.k8s import main as k8s
from lib.k8s import settings as k8s_settings
from lib.ocp import settings as ocp_settings
from lib.k8s import output as k8s_output

from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cluster")
@click.pass_obj
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify api access")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_cluster(
        ctx,
        verify,
        output,
        devel
        ):
    """Get k8s cluster settings"""

    # iserver get k8s cluster

    ctx.developer = devel
    ctx.output = output

    try:
        k8s_settings_handler = k8s_settings.K8sSettings(log_id=ctx.run_id)
        ocp_settings_handler = ocp_settings.OcpSettings(log_id=ctx.run_id)
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)

        clusters = k8s_settings_handler.get_k8s_clusters()

        if clusters is None or len(clusters) == 0:
            ctx.my_output.default('No kubernetes clusters defined')
            return

        default_cluster_name = k8s_settings_handler.get_default_cluster()
        for cluster in clusters:
            cluster['__Output'] = {}

            if default_cluster_name is not None and cluster['name'] == default_cluster_name:
                cluster['__Output']['defaultTick'] = 'Green'
                cluster['defaultTick'] = '\u2713'

            for key in ['virtctl', 'helm', 'tools']:
                cluster[key] = None

            if cluster['type'] == 'ocp' and cluster['source'] == 'import':
                ocp_cluster = ocp_settings_handler.get_ocp_cluster(
                    cluster['name']
                )
                if ocp_cluster is not None:
                    for key in ['virtctl', 'helm', 'tools']:
                        cluster[key] = ocp_cluster[key]
                        if cluster[key] is not None:
                            cluster[key]['description'] = '%s@%s' % (
                                cluster[key]['username'],
                                cluster[key]['ip']
                            )

        if verify:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

            for cluster in clusters:
                cluster['__Output']['apiTick'] = 'Red'
                cluster['apiTick'] = '\u2717'

                k8s_handler = k8s.K8s(kubeconfig_filename=cluster['kubeconfig'], cluster_type=cluster['type'], log_id=ctx.run_id)
                if k8s_handler.get_api() is not None:
                    cluster['__Output']['apiTick'] = 'Green'
                    cluster['apiTick'] = '\u2713'

            ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    clusters,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(clusters)

        k8s_output_handler.print_clusters(
            clusters,
            title=True
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
