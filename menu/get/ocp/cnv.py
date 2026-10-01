import sys
import click
from menu import validations
from lib.workflow.ocp_cnv_operator import get


@click.command("cnv")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--view", "-v", default=['state'], help="[state|import|crd]", show_default=True, multiple=True)
def get_ocp_cnv_command(ctx, cluster_names, view):
    """Get cnv operator in openshift cluster"""

    params = {}
    params['cluster'] = cluster_names
    params['view'] = view

    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default('View: state (def), import, crd', before_newline=True)