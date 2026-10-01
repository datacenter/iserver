import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("cnv")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'import', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--wipe", is_flag=True, default=False, show_default=True, help="Wipe dv/pvc")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cnv_command(ctx, cluster_names, mode, wipe, no_confirm):
    """Delete cnv operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}

    if mode in ['instance', 'all']:
        task['instance'] = {}

    if mode in ['import']:
        task['import'] = {}
        task['import']['wipe'] = wipe

    success = ocp_common.delete_workflow(cluster_names, 'cnv', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)