import sys
import traceback
import click

from menu import defaults
from menu import validations
from lib.workflow.ocp_imm import configure as ocp_workflow


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("imm")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
def set_ocp_imm_command(ctx, iaccount, cluster_name):
    """Set openshift cluster nodes to server mapping using Intersight"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['iaccount'] = iaccount

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
