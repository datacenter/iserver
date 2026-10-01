import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("hubble")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['relay', 'timescape'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cilium_hubble_command(ctx, cluster_names, mode, no_confirm):
    """Delete cilium hubble"""

    task = {}

    if mode in ['timescape']:
        task['timescape'] = {}

    if mode in ['relay']:
        task['relay'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'cilium-hubble', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)