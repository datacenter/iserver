import sys
import threading
import traceback
import click

from lib.k8s import output as k8s_output

from menu import validations
from menu import progress
from menu.common import get_confirmation


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("locvs")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
def delete_k8s_locvs_command(
        ctx,
        cluster
        ):
    """Delete k8s local volume set (ocp)"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, cluster_type='ocp', log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if k8s_handlers.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit

        locvs = k8s_handlers.get_local_volume_sets(pv_info=True, cache_enabled=False)

        ctx.busy = False

        success = k8s_handlers.delete_local_volume_sets(
            locvs,
            my_output=ctx.my_output,
            k8s_output=k8s_output_handler,
            confirmation=True,
            wait=True
        )
        if not success:
            raise ErrorExit


    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
