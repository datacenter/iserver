import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_cni import get_config as ocp_workflow

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("config")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--view", "-v", default=['config'], help="[config|map|state|all]", show_default=True, multiple=True)
def get_ocp_cilium_config_command(ctx, cluster_name, view):
    """Get cilium configuration"""

    view = validations.validate_view(
        ctx,
        view,
        'config|map|state|all',
        'config',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        params = {}
        params['cluster'] = cluster_name
        params['config'] = 'config' in view
        params['map'] = 'map' in view
        params['state'] = 'state' in view

        success = ocp_workflow.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

        ctx.my_output.default('View (-v): config (def), map, state, all', before_newline=True)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
