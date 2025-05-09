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


@click.command("node")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--label", default='', callback=validations.empty_string_to_none, help="Filter by label")
@click.option("--view", "-v", default=['state'], help="[state|ver|cap|label|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_node_command(
        ctx,
        cluster,
        name,
        label,
        view,
        output,
        devel
        ):
    """Get k8s node"""

    # iserver get k8s node

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|ver|cap|label|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster)
        if k8s_handlers is None:
            raise ErrorExit

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if label is not None:
            object_filter.append(
                'label:%s' % (label)
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
            nodes = k8s_handlers.get_nodes(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    nodes,
                    indent=4
                )
            )
            return

        nodes = k8s_handlers.get_nodes(
            object_filter=object_filter
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    nodes,
                    indent=4
                )
            )
            return

        if 'state' in view:
            k8s_output_handler.print_nodes_state(
                nodes,
                title=True
            )

        if 'ver' in view:
            k8s_output_handler.print_nodes_version(
                nodes,
                title=True
            )

        if 'cap' in view:
            k8s_output_handler.print_nodes_capacity(
                nodes,
                title=True
            )

        if 'label' in view:
            k8s_output_handler.print_nodes_label(
                nodes,
                title=True
            )

        ctx.my_output.default('Filter: name, label', before_newline=True)
        ctx.my_output.default('View:   state (def), ver, cap, label, all')

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
