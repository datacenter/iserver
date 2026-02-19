import sys
import json
import threading
import traceback
import click

from lib.k8s import output as k8s_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("locv")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--name", "-n", default='', callback=validations.empty_string_to_none, show_default=True, help="Filter by local volume name")
@click.option("--mode", type=click.Choice(['block', 'fs', 'any'], case_sensitive=False), default='any', show_default=True, help="Filter by local volume mode")
@click.option("--node", default='', callback=validations.empty_string_to_none, show_default=True, help="Filter by node name")
@click.option("--sc", "storage_class", default='', callback=validations.empty_string_to_none, show_default=True, help="Filter by storage class name")
@click.option("--device", default='', callback=validations.empty_string_to_none, show_default=True, help="Filter by device wwn")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_locv_command(
        ctx,
        cluster,
        name,
        mode,
        node,
        storage_class,
        device,
        view,
        output,
        devel
        ):
    """Get k8s local volume (ocp)"""

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, cluster_type='ocp', log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        if output not in ['json', 'mo']:
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

        if output == 'mo':
            locvs = k8s_handlers.get_local_volumes(
                object_filter=object_filter,
                return_mo=True,
                cache_enabled=False
            )
            ctx.my_output.default(
                json.dumps(
                    locvs,
                    indent=4
                )
            )
            return

        locvs = k8s_handlers.get_local_volumes(
            pv_info=True, 
            object_filter=object_filter,
            cache_enabled=False
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    locvs,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(locvs)

        if 'state' in view:
            k8s_output_handler.print_local_volumes(
                locvs,
                title=True
            )

            pvs = []
            for lvs in locvs:
                if lvs['pv'] is not None:
                    pvs.append(lvs['pv'])

            if len(pvs) > 0:
                ctx.my_output.default(
                    'Associated Persistent Volumes', 
                    underline=True, 
                    before_newline=True,
                    after_newline=True
                )
                k8s_output_handler.print_pvs(pvs)

        ctx.my_output.default('Filter: --', before_newline=True)
        ctx.my_output.default('View:   state (def)')

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
