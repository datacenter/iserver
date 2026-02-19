import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_gpu_operator import operator_create
from lib.workflow.ocp_gpu_operator import policy_create
from lib.workflow.ocp_gpu_operator import dashboard_create

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("gpu")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="NVIDIA Cluster Policy")
@click.option("--mode", type=click.Choice(['operator', 'policy', 'dashboard', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_gpu_command(
        ctx,
        cluster_name,
        channel,
        filename,
        mode,
        no_confirm
    ):
    """Set gpu operator in openshift cluster"""

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

        if mode in ['policy', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['filename'] = filename
            params['confirmation'] = not no_confirm

            success = policy_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['dashboard', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm

            success = dashboard_create.run(
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
