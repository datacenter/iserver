import sys
import traceback
import click

from lib.workflow.ocp_ntp import get as ocp_workflow

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ntp")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.validate_ocp_cluster_name_no_prompt, help="Cluster name")
def get_ocp_ntp_command(
        ctx,
        cluster_name
        ):
    """Get ocp ntp state"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        params = {}
        params['cluster'] = cluster_name

        success = ocp_workflow.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
