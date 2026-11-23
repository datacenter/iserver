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


@click.command("cconf")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--name", callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_cconf_command(
        ctx,
        cluster,
        name,
        view,
        output,
        devel
        ):
    """Get k8s cilium config"""

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

        if output == 'mo':
            cconf = k8s_handlers.get_cilium_config(
                name=name,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    cconf,
                    indent=4
                )
            )
            return

        cconf = k8s_handlers.get_cilium_config(name=name)

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    cconf,
                    indent=4
                )
            )
            return

        if 'state' in view:
            k8s_output_handler.print_cilium_config(
                cconf
            )

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
