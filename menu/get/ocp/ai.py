import sys
import click
from menu import validations
from lib.workflow.ocp_ai_operator import get


@click.command("ai")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--view", "-v", default=['state'], help="[state|res|all]", show_default=True, multiple=True)
def get_ocp_ai_command(ctx, cluster_names, view):
    """Get ai operator in openshift cluster"""

    params = {}
    params['cluster'] = cluster_names
    params['view'] = view

    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default('View: state (def), res, all', before_newline=True)