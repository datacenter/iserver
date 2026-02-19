import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_virtual_machine import cpu as ocp_workflow


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cpu")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--namespace", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="Virtual machine namespace")
@click.option("--name", default='', show_default=False, callback=validations.empty_string_to_none, help="Virtual machine name")
@click.option("--sockets", type=click.INT, default=1, help="Socket count")
@click.option("--cores", type=click.INT, default=1, help="Cores count")
@click.option("--threads", type=click.INT, default=1, help="Threads count")
@click.option("--restart", is_flag=True, show_default=True, default=False, help="Restart if required")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_k8s_vm_cpu(
        ctx,
        cluster_name,
        namespace,
        name,
        sockets,
        cores,
        threads,
        restart,
        no_confirm
        ):
    """Start vm"""

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['namespace'] = namespace
        params['name'] = name
        params['sockets'] = sockets
        params['cores'] = cores
        params['threads'] = threads
        params['restart'] = restart
        params['confirmation'] = not no_confirm

        success = ocp_workflow.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
