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


@click.command("package")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--installed", is_flag=True, show_default=True, default=False, help="Filter installed")
@click.option("--view", "-v", default=['state'], help="[state|desc]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_package_command(
        ctx,
        cluster,
        name,
        installed,
        view,
        output,
        devel
        ):
    """Get k8s package"""

    # iserver get k8s package

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|desc',
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
        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if installed:
            object_filter.append(
                'installed:true'
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
            packages = k8s_handlers.get_packages(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    packages,
                    indent=4
                )
            )
            return

        packages = k8s_handlers.get_packages(
            object_filter=object_filter,
            subscription_info=True
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    packages,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(packages)

        if 'state' in view:
            k8s_output_handler.print_packages(
                packages,
                title=True
            )

        if 'desc' in view:
            k8s_output_handler.print_packages(
                packages,
                title=True,
                description=True
            )

        ctx.my_output.default('Filter: name, installed', before_newline=True)
        ctx.my_output.default('View:   state (def), desc')

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
