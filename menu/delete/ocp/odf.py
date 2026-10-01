import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("odf")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'cluster', 'all'], case_sensitive=False), default='operator', show_default=True, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_odf_command(ctx, cluster_names, mode, no_confirm):
    """Delete odf operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}

    if mode in ['cluster', 'all']:
        task['cluster'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'odf', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)