import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("intersight")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'ui', 'register', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--ucs-tool", is_flag=True, show_default=True, default=False, help="Enable OsDiscoveryToolInstall")
@click.option("--client-id", default='', callback=validations.empty_string_to_none, help="Intersight client id")
@click.option("--client-secret", default='', callback=validations.empty_string_to_none, help="Intersight client secret")
@click.option("--location", type=click.Choice(['us', 'eu', 'va'], case_sensitive=False), default='us', show_default=True, help="Intersight server location")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_intersight_command(ctx, cluster_names, channel, mode, ucs_tool, client_id, client_secret, location, no_confirm):
    """Set intersight operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}
        task['operator']['channel'] = channel

    if mode in ['instance', 'all']:
        task['instance'] = {}
        task['instance']['ucs-tool'] = ucs_tool

    if mode in ['ui', 'all']:
        task['ui'] = {}

    if mode in ['register', 'all']:
        task['register'] = {}
        task['client-id'] = client_id
        task['client-secret'] = client_secret
        task['location'] = location

    success = ocp_common.set_workflow(cluster_names, 'intersight', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)