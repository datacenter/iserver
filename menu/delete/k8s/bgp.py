import sys
import threading
import traceback
import click

from lib.k8s import output as k8s_output

from menu import validations
from menu import progress
from progress.bar import Bar


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("bgp")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
def delete_k8s_bgp_command(
        ctx,
        cluster
        ):
    """Delete k8s bgp settings"""

    # iserver delete k8s bgp

    ctx.developer = False
    ctx.output = 'default'

    try:
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

        if not k8s_handlers.delete_isovalent_bgp_cluster_configs():
            ctx.busy = False
            ctx.my_output.error('Failed to delete isovalent bgp cluster configs')
            raise ErrorExit

        if not k8s_handlers.delete_isovalent_bgp_peer_configs():
            ctx.busy = False
            ctx.my_output.error('Failed to delete isovalent bgp peer configs')
            raise ErrorExit

        if not k8s_handlers.delete_isovalent_bgp_advertisements():
            ctx.busy = False
            ctx.my_output.error('Failed to delete isovalent bgp advertisements')
            raise ErrorExit

        ctx.busy = False
        ctx.my_output.default('Done')

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
