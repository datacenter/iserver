import sys
import click
from menu import validations
from lib.workflow.ocp_cilium_pnet import get


@click.command("pnet")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--view", "-v", default=['state'], help="[state|res|webhook|db|ep|all]", show_default=True, multiple=True)
def get_ocp_cilium_pnet_command(ctx, cluster_names, view):
    """Get cilium cluster private network"""

    params = {}
    params['cluster'] = cluster_names
    params['view'] = view

    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default('View: state (def), res, webhook, db, ep, all', before_newline=True)