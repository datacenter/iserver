import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("shutdown")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--node", multiple=True, help="Node name")
@click.option("--no-checks", is_flag=True, show_default=True, default=False, help="Skip checks")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode in case of eviction problems")
def set_ocp_node_shutdown_command(
        ctx,
        cluster_names,
        node,
        no_checks,
        no_confirm
        ):
    """Set k8s node graceful shutdown"""

    task = {}
    task['shutdown'] = {}
    task['shutdown']['node'] = node
    task['shutdown']['checks'] = not no_checks

    success = ocp_common.set_workflow(cluster_names, 'ocp-node', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)