import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("terminal")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_terminal(
        ctx,
        cluster_names,
        no_confirm
        ):
    """Set ocp cluster web terminal"""

    task = {}
    task['operator'] = {}
    
    success = ocp_common.set_workflow(cluster_names, 'terminal', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)