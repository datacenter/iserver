import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_ai_operator import operator_delete 
from lib.workflow.ocp_ai_operator import cluster_delete 

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ai")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'cluster', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--dsc", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="Data Science Cluster")
def delete_ocp_ai_command(ctx, cluster_name, mode, dsc):
    """Delete data science (ai) operator in openshift cluster"""

    try:
        if mode in ['cluster', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['dsc'] = dsc

            success = cluster_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name

            success = operator_delete.run(
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
