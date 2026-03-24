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


@click.command("pod")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--namespace", "-n", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--owner", default='', callback=validations.empty_string_to_none, help="Filter by owner")
@click.option("--node", default='', callback=validations.empty_string_to_none, help="Filter by node")
@click.option("--view", "-v", default=['state'], help="[state|metadata|cont|res|svc|env|cm|vol|net|log|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_pod_command(
        ctx,
        cluster,
        namespace,
        name,
        owner,
        node,
        view,
        output,
        devel
        ):
    """Get k8s pod"""

    # iserver get k8s pod

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|metadata|cont|res|svc|env|cm|vol|net|log|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        object_filter = []
        call_namespace = None
        if namespace is not None:
            if '*' in namespace:
                object_filter.append(
                    'namespace:%s' % (namespace)
                )
            else:
                call_namespace = namespace

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if owner is not None:
            object_filter.append(
                'owner:%s' % (owner)
            )

        if node is not None:
            object_filter.append(
                'node:%s' % (node)
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
            pods = k8s_handlers.get_pods(
                namespace=call_namespace,
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    pods,
                    indent=4
                )
            )
            return

        service_info = False
        log_info = False

        if 'state' in view:
            service_info = True

        if 'svc' in view:
            service_info = True

        if 'log' in view:
            log_info = True

        pods = k8s_handlers.get_pods(
            namespace=call_namespace,
            object_filter=object_filter,
            service_info=service_info,
            log_info=log_info
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    pods,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(pods)
        
        if 'state' in view:
            k8s_output_handler.print_pods_state(pods)

        if 'metadata' in view:
            k8s_output_handler.print_pods_metadata(pods)

        if 'cont' in view:
            k8s_output_handler.print_pods_container(
                pods,
                title=True
            )

        if 'res' in view:
            k8s_output_handler.print_pods_resource(
                pods,
                title=True
            )

        if 'svc' in view:
            k8s_output_handler.print_pods_service(
                pods,
                title=True
            )

        if 'env' in view:
            k8s_output_handler.print_pods_env(
                pods,
                title=True
            )

        if 'cm' in view:
            k8s_output_handler.print_pods_cm(
                pods,
                title=True
            )

        if 'vol' in view:
            k8s_output_handler.print_pods_vol(
                pods,
                title=True
            )

        if 'net' in view:
            k8s_output_handler.print_pods_net(
                pods
            )

        if 'log' in view:
            k8s_output_handler.print_pods_log(
                pods,
                title=True
            )

        ctx.my_output.default('Filter: namespace, name, owner', before_newline=True)
        ctx.my_output.default('View:   state (def), metadata, cont, res, svc, env, cm, vol, net, log, all')

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
