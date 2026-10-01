import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("lvm")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'cluster', 'all', 'orphan', 'unused'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--no-wipe", is_flag=True, default=False, show_default=True, help="Wipe lvm from disks")
@click.option("--no-zap", is_flag=True, default=False, show_default=True, help="Wipe filesystem from lvm disks")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_lvm_command(ctx, cluster_names, mode, no_wipe, no_zap, no_confirm):
    """Delete logical volume manager storage operator in openshift cluster"""

    task = {}

    if mode == 'orphan':
        task['orphan'] = {}

    if mode == 'unused':
        task['unused'] = {}
        
    if mode in ['cluster', 'all']:
        task['cluster'] = {}
        task['cluster']['wipe'] = not no_wipe
        task['cluster']['zap'] = not no_zap

    if mode in ['operator', 'all']:
        task['operator'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'lvm', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)