import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("grafana")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'mon', 'instance', 'wipe', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--instance", default='', callback=validations.empty_string_to_none, show_default=True, help="Grafana instance name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_grafana_command(ctx, cluster_names, mode, instance, no_confirm):
    """Delete grafana operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}

    if mode in ['instance', 'all']:
        task['instance'] = {}
        task['instance']['instance'] = instance

    if mode in ['wipe', 'all']:
        task['wipe'] = {}

    if mode in ['mon', 'all']:
        task['mon'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'grafana', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)