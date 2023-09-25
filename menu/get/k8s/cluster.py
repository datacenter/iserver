import sys
import threading
import traceback
import click

from lib.k8s import main as k8s
from lib.k8s import settings

from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cluster")
@click.pass_obj
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify api access")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_cluster(
        ctx,
        verify,
        devel
        ):
    """Get k8s cluster settings"""

    # iserver get k8s cluster

    ctx.developer = devel

    try:
        settings_handler = settings.K8sSettings(log_id=ctx.run_id)
        clusters = settings_handler.get_k8s_clusters()

        if clusters is None or len(clusters) == 0:
            ctx.my_output.default('No kubernetes clusters defined')
            return

        default_cluster_name = settings_handler.get_default_cluster()
        if default_cluster_name is not None:
            for cluster in clusters:
                cluster['__Output'] = {}
                if cluster['name'] == default_cluster_name:
                    cluster['__Output']['defaultTick'] = 'Green'
                    cluster['defaultTick'] = '\u2713'

        if verify:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

            for cluster in clusters:
                cluster['__Output'] = {}
                cluster['__Output']['apiTick'] = 'Red'
                cluster['apiTick'] = '\u2717'

                k8s_handler = k8s.K8s(kubeconfig_filename=cluster['kubeconfig'], cluster_type=cluster['type'], log_id=ctx.run_id)
                if k8s_handler.get_api() is not None:
                    cluster['__Output']['apiTick'] = 'Green'
                    cluster['apiTick'] = '\u2713'

            ctx.busy = False

        order = [
            'name',
            'defaultTick',
            'type',
            'kubeconfig',
        ]

        headers = [
            'Cluster Name',
            'Default',
            'Type',
            'Kubeconfig'
        ]

        if verify:
            order.append('apiTick')
            headers.append('API')

        ctx.my_output.my_table(
            clusters,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
