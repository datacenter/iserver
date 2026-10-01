import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("plan")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_plan_command(ctx, cluster_names, no_confirm):
    """Set cilium cni install plan"""

    task = {}
    task['approve'] = {}

    success = ocp_common.set_workflow(cluster_names, 'cilium', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)