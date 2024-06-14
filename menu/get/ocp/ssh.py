import sys
import traceback
import threading
import click

from lib.ocp import output as ocp_output

from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ssh")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Filter by cluster name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_ssh_command(
        ctx,
        cluster_name,
        output,
        devel
        ):
    """Get ocp nodes ssh access"""

    # iserver get ocp ssh

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type='ocp')
        if k8s_handlers is None:
            raise ErrorExit

        ocp_output_handler = ocp_output.OcpOutput(log_id=ctx.run_id)
        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name
        )
        if ocp_handler is None:
            raise ErrorExit

        keys = ocp_handler.get_ocp_ssh_authorized_keys()
        ctx.busy = False
        ocp_output_handler.print_ocp_ssh_authorized_keys(keys)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
