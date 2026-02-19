import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cni import get

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cni")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
def get_ocp_cni_command(ctx, cluster_name):
    """Get cni in openshift cluster"""

    try:
        params = {}
        params['cluster'] = cluster_name

        success = get.run(
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
