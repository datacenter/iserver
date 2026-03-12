import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_oauth import get as ocp_workflow

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("oauth")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--view", "-v", default=['state'], help="[state|verbose]", show_default=True, multiple=True)
def get_ocp_oauth_command(ctx, cluster_name, view):
    """Get oauth in openshift cluster"""

    view = validations.validate_view(
        ctx,
        view,
        'state|verbose',
        'state',
        []
    )
    
    try:
        params = {}
        params['cluster'] = cluster_name
        params['view'] = view

        success = ocp_workflow.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

        ctx.my_output.default('View: state (def), verbose', before_newline=True)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
