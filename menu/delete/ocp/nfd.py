import sys
import click
from lib.workflow import ocp_common
from menu import validations

@click.command("nfd")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'all'], case_sensitive=False), callback=validations.validate_option, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_nfd_command(ctx, cluster_names, mode, no_confirm):
    """Delete nfd operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}

    if mode in ['instance', 'all']:
        task['instance'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'nfd', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)