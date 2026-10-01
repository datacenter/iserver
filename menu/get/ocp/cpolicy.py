import sys
import click
from lib.workflow.ocp_container_runtime_policy import get
from menu import validations


@click.command("cpolicy")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.validate_ocp_cluster_name_no_prompt, help="Cluster name")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
def get_ocp_cpolicy_command(ctx, cluster_names, view):
    """Get ocp container policy"""

    params = {}
    params['cluster'] = cluster_names
    params['view'] = view

    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default('View: state (def)', before_newline=True)