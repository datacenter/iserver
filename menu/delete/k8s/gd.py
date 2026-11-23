import sys
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


@click.command("gd")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--instance", default='', callback=validations.empty_string_to_none, help="Filter by grafana instance")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_k8s_gd_command(
        ctx,
        cluster,
        namespace,
        name,
        instance,
        no_confirm
        ):
    """Delete k8s grafana dashboard"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, log_id=ctx.run_id)
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
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

        if instance is not None:
            object_filter.append(
                'instance:%s' % (instance)
            )

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if k8s_handlers.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit

        dashboards = k8s_handlers.get_grafana_dashboards(
            object_filter=object_filter,
            instance_info=True,
            cache_enabled=False
        )

        ctx.busy = False

        if len(dashboards) == 0:
            ctx.my_output.default('No object found', before_newline=True)
            return

        k8s_output_handler.print_grafana_dashboards(dashboards)

        if not no_confirm:
            value = input('Confirm (Y/N) ')
            if value.lower() != 'y':
                return

        for dashboard in dashboards:
            success = k8s_handlers.delete_grafana_dashboard(
                dashboard['namespace'],
                dashboard['name'],
                my_output=ctx.my_output
            )
            if not success:
                raise ErrorExit

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
