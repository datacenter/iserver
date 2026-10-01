import sys
import click
from menu import validations
from lib.workflow.ocp_cilium_mesh import get


@click.command("mesh")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--view", "-v", default=['state'], help="[state|config|all]", show_default=True, multiple=True)
def get_ocp_cilium_mesh_command(ctx, cluster_names, view):
    """Get cilium cluster mesh"""

    params = {}
    params['cluster'] = cluster_names
    params['view'] = view

    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default('View: state (def), config, all', before_newline=True)