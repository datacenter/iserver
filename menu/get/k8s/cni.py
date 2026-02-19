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


@click.command("cni")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
def get_k8s_cni_command(
        ctx,
        cluster,
        output
        ):
    """Get k8s cni"""

    ctx.developer = False
    ctx.output = output

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
            cnis = k8s_handlers.get_cnis(
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    cnis,
                    indent=4
                )
            )
            return

        cnis = k8s_handlers.get_cnis()

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    cnis,
                    indent=4
                )
            )
            return

        k8s_output_handler.print_cnis(cnis)

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
