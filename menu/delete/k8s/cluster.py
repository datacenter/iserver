import sys
import threading
import traceback
import click

from lib.k8s import settings

from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cluster")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', help="K8s cluster name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_k8s_cluster(
        ctx,
        cluster_name,
        devel
        ):
    """Delete k8s cluster"""

    # iserver delete k8s cluster

    ctx.developer = devel

    try:
        settings_handler = settings.K8sSettings(log_id=ctx.run_id)
        cluster = settings_handler.get_k8s_cluster(cluster_name)

        if cluster is None:
            ctx.my_output.default('Kubernetes cluster not defined')
            raise ErrorExit

        if cluster['source'] != 'user':
            ctx.my_output.default('Kubernetes cluster cannot be deleted')
            raise ErrorExit

        if not settings_handler.delete_k8s_cluster(cluster_name):
            ctx.my_output.default('Kubernetes cluster delete failed')
            raise ErrorExit

        ctx.my_output.default('Kubernetes cluster deleted')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
