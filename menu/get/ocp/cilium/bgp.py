import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_bgp import get as ocp_workflow

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("bgp")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--view", "-v", default=['state'], help="[cli|crd|state]", show_default=True, multiple=True)
def get_ocp_cilium_bgp_command(ctx, cluster_name, view):
    """Get cilium bgp control plane"""

    view = validations.validate_view(
        ctx,
        view,
        'cli|crd|state',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        params = {}
        params['cluster'] = cluster_name
        params['cli'] = 'cli' in view
        params['crd'] = 'crd' in view
        params['state'] = 'state' in view

        success = ocp_workflow.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

        ctx.my_output.default('View (-v): state (def), cli, crd', before_newline=True)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
