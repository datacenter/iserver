import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("cli-cilium")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cli_cilium(
        ctx,
        cluster_names,
        no_confirm
        ):
    """Set ocp cluster cilium"""

    task = {}
    task['cilium'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'cli', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)