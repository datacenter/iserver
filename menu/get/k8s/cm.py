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


@click.command("cm")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--cname", default='', callback=validations.empty_string_to_none, help="Filter by cm name")
@click.option("--cdata", default='', callback=validations.empty_string_to_none, help="Filter by cm data")
@click.option("--view", "-v", default=['state'], help="[state|name|data|pod|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_cm_command(
        ctx,
        cluster,
        namespace,
        name,
        cname,
        cdata,
        view,
        output,
        devel
        ):
    """Get k8s config map"""

    # iserver get k8s cm

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|name|data|pod|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, cluster_type='ocp')
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

        if cname is not None:
            object_filter.append(
                'cm-name:%s' % (cname)
            )

        if cdata is not None:
            object_filter.append(
                'cm-data:%s' % (cdata)
            )

        if output not in ['json', 'mo']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if k8s_handlers.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit

        if output == 'mo':
            config_maps = k8s_handlers.get_config_maps(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    config_maps,
                    indent=4
                )
            )
            return

        pod_info = False
        if 'pod' in view:
            pod_info = True

        config_maps = k8s_handlers.get_config_maps(
            object_filter=object_filter,
            pod_info=pod_info
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    config_maps,
                    indent=4
                )
            )
            return

        if 'state' in view:
            k8s_output_handler.print_config_maps(
                config_maps,
                title=True
            )

        if 'name' in view:
            k8s_output_handler.print_config_maps_name(
                config_maps,
                title=True
            )

        if 'data' in view:
            k8s_output_handler.print_config_maps_data(
                config_maps,
                title=True
            )

        if 'pod' in view:
            k8s_output_handler.print_config_maps_pod(
                config_maps,
                title=True
            )

        ctx.my_output.default('Filter: namespace, name, cname, cdata', before_newline=True)
        ctx.my_output.default('View:   state (def), name, data, pod, all')

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
