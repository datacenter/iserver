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


@click.command("promtarget")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by service monitor namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by service monitor name")
@click.option("--type", "target_type", type=click.Choice(['all', 'platform', 'user'], case_sensitive=False), default='all', show_default=True)
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def get_k8s_promtarget_command(
        ctx,
        cluster,
        namespace,
        name,
        target_type,
        view,
        output
        ):
    """Get k8s prometheus target"""

    ctx.developer = False
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

        object_filter = []

        if namespace is not None:
            object_filter.append(
                'namespace:%s' % (namespace)
            )

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if target_type == 'platform':
            object_filter.append(
                'type:P'
            )

        if target_type == 'user':
            object_filter.append(
                'type:U'
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if k8s_handlers.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit

        prometheus_targets = k8s_handlers.get_prometheus_targets(
            object_filter=object_filter
        )

        ctx.busy = False

        ctx.my_output.json_output(prometheus_targets)

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    prometheus_targets,
                    indent=4
                )
            )
            return

        if 'state' in view:
            k8s_output_handler.print_prometheus_targets(prometheus_targets)

        ctx.my_output.default('Filter: namespace, name', before_newline=True)
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
