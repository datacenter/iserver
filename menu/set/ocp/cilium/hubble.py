import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("hubble")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['relay', 'timescape'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--insecure", is_flag=True, show_default=True, default=False, help="Insecure route")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_hubble_command(ctx, cluster_names, mode, insecure, no_confirm):
    """Set cilium hubble"""

    task = {}

    if mode in ['relay']:
        task['relay'] = {}

    if mode in ['timescape']:
        task['timescape'] = {}
        task['timescape']['insecure'] = insecure

    success = ocp_common.set_workflow(cluster_names, 'cilium-hubble', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)