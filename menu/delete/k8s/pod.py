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


@click.command("pod")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="No wait mode")
def delete_k8s_pod_command(
        ctx,
        cluster,
        namespace,
        name,
        no_confirm,
        no_wait
        ):
    """Delete k8s pod"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        object_filter = []
        if namespace is not None:
            object_filter.append(
                'namespace:%s' % (namespace)
            )

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if k8s_handlers.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit

        success = k8s_handlers.delete_pods(
            object_filter,
            confirmation=not no_confirm,
            my_output=ctx.my_output,
            k8s_output=k8s_output_handler,
            wait=not no_wait
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
