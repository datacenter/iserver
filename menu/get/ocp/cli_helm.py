import sys
import click
from lib.workflow.ocp_cli import helm_get as get
from menu import validations


@click.command("cli-helm")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--view", "-v", default=['list'], help="[list|ver|all]", show_default=True, multiple=True)
def get_ocp_cli_helm(ctx, cluster_names, view):
    """Get ocp cluster helm"""

    params = {}
    params['cluster'] = cluster_names
    params['view'] = view

    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default('View: list (def), ver, all', before_newline=True)