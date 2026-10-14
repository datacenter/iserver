import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("splunk")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--version", default='3.1.0', show_default=True, help="Operator version")
@click.option("--name", default='', callback=validations.empty_string_to_none, show_default=True, help="Standalone instance name")
@click.option("--etc-size", "etc_size", default='10Gi', show_default=True, help="etc volume size")
@click.option("--etc-sc", "etc_sc", default='', callback=validations.empty_string_to_none, show_default=True, help="etc storage class")
@click.option("--var-size", "var_size", default='100Gi', show_default=True, help="var volume size")
@click.option("--var-sc", "var_sc", default='', callback=validations.empty_string_to_none, show_default=True, help="var storage class")
@click.option("--sa", default='default', show_default=True, help="service account")
@click.option("--no-route", is_flag=True, show_default=True, default=False, help="Instance route")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_splunk_command(ctx, cluster_names, mode, version, name, etc_size, etc_sc, var_size, var_sc, sa, no_route, no_confirm):
    """Set splunk enterprise operator in openshift cluster"""

    task = {}
    if mode in ['operator']:
        task['operator'] = {}
        task['operator']['version'] = version

    if mode in ['instance']:
        task['instance'] = {}
        task['instance']['instance'] = []
        item = {}
        item['name'] = name
        item['etc-size'] = etc_size
        item['etc-sc'] = etc_sc
        item['var-size'] = var_size
        item['var-sc'] = var_sc
        item['sa'] = sa
        item['route'] = not no_route
        task['instance']['instance'].append(item)
        
    success = ocp_common.set_workflow(cluster_names, 'splunk', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)