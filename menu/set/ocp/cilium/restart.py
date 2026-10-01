import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("restart")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'agent', 'all'], case_sensitive=False), default='all', show_default=True, help="Mode of operation")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_restart_command(ctx, cluster_names, mode, no_wait, no_confirm):
    """Restart cilium components"""

    task = {}
    task['restart'] = {}
    task['restart']['operator'] = mode in ['operator', 'all']
    task['restart']['agent'] = mode in ['agent', 'all']
    task['restart']['wait'] = not no_wait

    success = ocp_common.set_workflow(cluster_names, 'cilium', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)