import os
import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cli import apply as task_handler


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("file")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, show_default=True, help="Namespace name")
@click.option("--location", multiple=True, help="YAML crds location")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_file_command(
        ctx, 
        cluster_name, 
        namespace,
        location,
        no_confirm
    ):
    """Set openshift crds from file(s)"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['namespace'] = namespace
        params['location'] = []
        for item in location:
            params['location'].append(item)
        params['confirmation'] = not no_confirm
        
        success = task_handler.run(
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
