import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("splunk")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--instance", default='', callback=validations.empty_string_to_none, show_default=True, help="Standalone instance name")
@click.option("--no-route", is_flag=True, show_default=True, default=False, help="Instance route")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_splunk_command(ctx, cluster_names, mode, channel, instance, no_route, no_confirm):
    """Set splunk enterprise operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}
        task['operator']['channel'] = channel

    if mode in ['instance', 'all']:
        task['instance'] = {}
        task['instance']['instance'] = instance
        task['instance']['route'] = not no_route
        
    success = ocp_common.set_workflow(cluster_names, 'splunk', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)