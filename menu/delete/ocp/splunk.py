import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_splunk_operator import operator_delete
from lib.workflow.ocp_splunk_operator import instance_delete

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("splunk")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--instance", multiple=True, help="Standalone instance name")
def delete_ocp_splunk_command(ctx, cluster_name, mode, instance):
    """Delete splunk operator in openshift cluster"""

    try:
        if mode in ['instance', 'all']:
            if mode == 'all':
                instance = ['__all__']
                
            params = {}
            params['cluster'] = cluster_name
            params['instance'] = instance

            success = instance_delete.run(
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
