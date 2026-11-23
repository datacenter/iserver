import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("gpu")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'policy', 'dashboard', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_gpu_command(
        ctx,
        cluster_names,
        mode,
        no_confirm
    ):
    """Delete gpu operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}

    if mode in ['policy', 'all']:
        task['policy'] = {}

    if mode in ['dashboard', 'all']:
        task['dashboard'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'gpu', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)