import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("splunk")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--name", multiple=True, help="Standalone instance name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_splunk_command(ctx, cluster_names, mode, name, no_confirm):
    """Delete splunk operator in openshift cluster"""

    task = {}
    if mode in ['operator']:
        task['operator'] = {}

    if mode in ['instance']:
        task['instance'] = {}
        task['instance']['instance'] = []
        for item in name:
            task_item = {}
            task_item['name'] = item
            task['instance']['instance'].append(task_item)

    success = ocp_common.delete_workflow(cluster_names, 'splunk', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)