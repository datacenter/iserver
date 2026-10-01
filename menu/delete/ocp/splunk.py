import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("splunk")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--instance", multiple=True, help="Standalone instance name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_splunk_command(ctx, cluster_names, mode, instance, no_confirm):
    """Delete splunk operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}

    if mode in ['instance', 'all']:
        task['instance'] = {}
        if mode == 'all':
            instance = ['__all__']

        task['instance']['instance'] = instance

    success = ocp_common.delete_workflow(cluster_names, 'splunk', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)