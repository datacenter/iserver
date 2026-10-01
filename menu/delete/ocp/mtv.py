import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("mtv")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'provider', 'smap', 'nmap', 'plan', 'wipe', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--wipe", is_flag=True, default=False, show_default=True, help="Wipe plans")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_mtv_command(ctx, cluster_names, mode, namespace, name, wipe, no_confirm):
    """Delete mtv operator in openshift cluster"""

    task = {}
    if mode in ['plan', 'wipe', 'all']:
        task['plan'] = {}
        task['plan']['namespace'] = namespace
        task['plan']['name'] = name
        task['plan']['wipe'] = wipe

    if mode in ['nmap', 'wipe', 'all']:
        task['nmap'] = {}
        task['nmap']['namespace'] = namespace
        task['nmap']['name'] = name

    if mode in ['smap', 'wipe', 'all']:
        task['smap'] = {}
        task['smap']['namespace'] = namespace
        task['smap']['name'] = name

    if mode in ['provider', 'wipe', 'all']:
        task['provider'] = {}
        task['provider']['name'] = name

    if mode in ['instance', 'all']:
        task['instance'] = {}

    if mode in ['operator', 'all']:
        task['operator'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'mtv', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)