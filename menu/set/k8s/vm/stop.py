import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_virtual_machine import stop as ocp_workflow


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("stop")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--namespace", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="Virtual machine namespace")
@click.option("--name", default='', show_default=False, callback=validations.empty_string_to_none, help="Virtual machine name")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="No wait")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_k8s_vm_stop(
        ctx,
        cluster_name,
        namespace,
        name,
        no_wait,
        no_confirm
        ):
    """Stop vm"""

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['namespace'] = namespace
        params['name'] = name
        params['wait'] = not no_wait
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
