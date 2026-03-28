import sys
import click
import traceback

from menu import validations
from lib.workflow.k8s import namespace_delete as workflow


class ErrorExit(Exception):
    pass


@click.command("ns")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Namespace name")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_k8s_ns_command(
        ctx,
        cluster_name,
        name,
        no_confirm
        ):
    """Delete k8s ns"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        params = {}
        params['cluster'] = cluster_name
        params['namespace'] = name
        params['confirmation'] = not no_confirm

        success = workflow.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)