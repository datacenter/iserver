import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cert_manager import feature_enable


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cert-manager")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
def set_ocp_cert_manager_command(ctx, cluster_name):
    """Set cert manager in openshift cluster"""

    try:
        params = {}
        params['cluster'] = cluster_name
        success = feature_enable.run(
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
