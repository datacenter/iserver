import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_vast_operator import get as ocp_workflow

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vast")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--view", "-v", default=['state'], help="[state|res|all]", show_default=True, multiple=True)
def get_ocp_vast_command(ctx, cluster_name, verbose, view):
    """Get vast csi operator in openshift cluster"""

    view = validations.validate_view(
        ctx,
        view,
        'state|res|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        params = {}
        params['cluster'] = cluster_name
        params['verbose'] = verbose
        params['view'] = view
        
        success = ocp_workflow.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

        ctx.my_output.default('View: state (def), res, all', before_newline=True)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
