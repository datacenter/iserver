import sys
import click
from menu import validations
from lib.workflow.ocp_cilium_cni import get_agent


@click.command("agent")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Agent name")
@click.option("--view", "-v", default=['pod'], help="[pod|logs|version]", show_default=True, multiple=True)
def get_ocp_cilium_agent_command(ctx, cluster_names, name, view):
    """Get cilium agent"""

    params = {}
    params['cluster'] = cluster_names
    params['agent'] = name
    params['view'] = view

    success = get_agent.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default('View: pod (def), logs, version', before_newline=True)