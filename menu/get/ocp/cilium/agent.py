import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_cni import get_agent

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("agent")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Agent name")
@click.option("--view", "-v", default=['pod'], help="[pod|logs|version]", show_default=True, multiple=True)
def get_ocp_cilium_agent_command(ctx, cluster_name, name, view):
    """Get cilium agent"""

    view = validations.validate_view(
        ctx,
        view,
        'pod|logs|version',
        'pod',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        params = {}
        params['cluster'] = cluster_name
        params['agent'] = name
        params['view'] = view

        success = get_agent.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

        ctx.my_output.default('View (-v): pod (def), logs, version', before_newline=True)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
