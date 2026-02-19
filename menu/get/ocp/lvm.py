import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_lvm_operator import get as ocp_workflow

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("lvm")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
def get_ocp_lvm_command(ctx, cluster_name, verbose):
    """Get logical volume manager storage operator in openshift cluster"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['ssh-check'] = True
        params['verbose'] = verbose
        
        success = ocp_workflow.run(
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
