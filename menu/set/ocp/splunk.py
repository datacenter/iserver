import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_splunk_operator import operator_create
from lib.workflow.ocp_splunk_operator import instance_create

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("splunk")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--instance", default='', callback=validations.empty_string_to_none, show_default=True, help="Standalone instance name")
@click.option("--no-route", is_flag=True, show_default=True, default=False, help="Instance route")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_splunk_command(ctx, cluster_name, mode, channel, instance, no_route, no_confirm):
    """Set splunk enterprise operator in openshift cluster"""

    try:
        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['channel'] = channel
            params['confirmation'] = not no_confirm
                
            success = operator_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['instance', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['instance'] = instance
            params['route'] = not no_route
            params['confirmation'] = not no_confirm
                
            success = instance_create.run(
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
