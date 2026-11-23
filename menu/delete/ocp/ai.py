import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("ai")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'cluster', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--dsc", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="Data Science Cluster")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_ai_command(ctx, cluster_names, mode, dsc, no_confirm):
    """Delete data science (ai) operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}

    if mode in ['cluster', 'all']:
        task['cluster'] = {}
        task['cluster']['dsc'] = dsc

    success = ocp_common.delete_workflow(cluster_names, 'ai', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)