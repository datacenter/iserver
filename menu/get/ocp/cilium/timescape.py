import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_timescape import get


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("timescape")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--view", "-v", default=['state'], help="[state|details]", show_default=True, multiple=True)
def get_ocp_cilium_timescape_command(ctx, cluster_name, view):
    """Get cilium cluster private network"""

    view = validations.validate_view(
        ctx,
        view,
        'state|details',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        params = {}
        params['cluster'] = cluster_name
        params['view'] = view

        success = get.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit         

        ctx.my_output.default(
            'View: state (def), details',
            before_newline=True
        )            

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
