import sys
import json
import threading
import traceback
import click

from lib import ip_helper
from lib.k8s import output as k8s_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("svc")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--type", "-t", "svc_type", type=click.Choice(['NodePort', 'ClusterIP', 'ExternalNane', 'LoadBalancer', 'any'], case_sensitive=False), default='any', show_default=True, help="Filter by type")
@click.option("--cluster-ip", default='', callback=validations.empty_string_to_none, help="Filter by cluster IP")
@click.option("--external-ip", default='', callback=validations.empty_string_to_none, help="Filter by external IP")
@click.option("--port", default='', callback=validations.validate_int_oper, help="Filter by port")
@click.option("--special", default='', callback=validations.empty_string_to_none, help="Filter by special selector")
@click.option("--view", "-v", default=['state'], help="[state|label|pod|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_svc_command(
        ctx,
        cluster,
        namespace,
        name,
        svc_type,
        cluster_ip,
        external_ip,
        port,
        special,
        view,
        output,
        devel
        ):
    """Get k8s service"""

    # iserver get k8s srv

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|label|pod|all',
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

        if namespace is not None:
            object_filter.append(
                'namespace:%s' % (namespace)
            )

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if svc_type != 'any':
            object_filter.append(
                'type:%s' % (svc_type)
            )

        if cluster_ip is not None:
            if ip_helper.is_valid_ipv4_address(cluster_ip):
                object_filter.append(
                    'cluster-ip:%s' % (cluster_ip)
                )
            else:
                if ip_helper.is_valid_ipv4_cidr(cluster_ip):
                    object_filter.append(
                        'cluster-subnet:%s' % (cluster_ip)
                    )
                else:
                    object_filter.append(
                        'cluster-string:%s' % (cluster_ip)
                    )

        if external_ip is not None:
            if ip_helper.is_valid_ipv4_address(external_ip):
                object_filter.append(
                    'external-ip:%s' % (external_ip)
                )
            else:
                if ip_helper.is_valid_ipv4_cidr(external_ip):
                    object_filter.append(
                        'external-subnet:%s' % (external_ip)
                    )
                else:
                    object_filter.append(
                        'external-string:%s' % (external_ip)
                    )

        if len(port) > 0:
            object_filter.append(
                'port:%s' % (port)
            )

        if special is not None:
            object_filter.append(
                'special:%s' % (special)
            )

        pod_info = False
        if 'pod' in view:
            pod_info = True

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
            services = k8s_handlers.get_services(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    services,
                    indent=4
                )
            )
            return

        services = k8s_handlers.get_services(
            object_filter=object_filter,
            pod_info=pod_info
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    services,
                    indent=4
                )
            )
            return

        if 'state' in view:
            k8s_output_handler.print_services(
                services,
                title=True
            )

        if 'label' in view:
            k8s_output_handler.print_services_label(
                services,
                title=True
            )

        if 'pod' in view:
            k8s_output_handler.print_services_pod(
                services,
                title=True
            )
        ctx.my_output.default('Filter: namespace, name, type, cluster-ip, external-ip, port, special', before_newline=True)
        ctx.my_output.default('View:   state (def), label, pod, all')

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
