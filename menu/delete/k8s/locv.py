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


@click.command("locv")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--name", "-n", default='', callback=validations.empty_string_to_none, show_default=True, help="Filter by local volume name")
@click.option("--mode", type=click.Choice(['block', 'fs', 'any'], case_sensitive=False), default='any', show_default=True, help="Filter by local volume mode")
@click.option("--node", default='', callback=validations.empty_string_to_none, show_default=True, help="Filter by node name")
@click.option("--sc", "storage_class", default='', callback=validations.empty_string_to_none, show_default=True, help="Filter by storage class name")
@click.option("--device", default='', callback=validations.empty_string_to_none, show_default=True, help="Filter by device wwn")
def delete_k8s_locv_command(
        ctx,
        cluster,
        name,
        mode,
        node,
        storage_class,
        device
        ):
    """Get k8s local volume (ocp)"""

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

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if mode != 'any':
            if mode == 'block':
                object_filter.append(
                    'mode:Block'
                )

            if mode == 'fs':
                object_filter.append(
                    'mode:Filesystem'
                )

        if node is not None:
            object_filter.append(
                'node:%s' % (node)
            )

        if storage_class is not None:
            object_filter.append(
                'sc:%s' % (storage_class)
            )

        if device is not None:
            object_filter.append(
                'device:%s' % (device)
            )

        locvs = k8s_handlers.get_local_volumes(
            pv_info=True, 
            object_filter=object_filter,
            cache_enabled=False
        )

        ctx.busy = False

        success = k8s_handlers.delete_local_volumes(
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
