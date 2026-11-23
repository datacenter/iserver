import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("iotel")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['instance', 'poller'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--suffix", default='', callback=validations.empty_string_to_none, help="Suffix name")
@click.option("--metric", multiple=True, help="Metric name")
@click.option("--attribute", multiple=True, help="Metric name")
@click.option("--wipe", is_flag=True, show_default=True, default=False, help="Wipe mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_iotel_command(ctx, cluster_names, mode, suffix, metric, attribute, wipe, no_confirm):
    """Delete openshift intersight open telemetry collector"""

    task = {}
    if mode in ['instance']:
        task['instance'] = {}
        task['instance']['suffix'] = suffix
        task['instance']['wipe'] = wipe

    if mode in ['poller']:
        task['poller'] = {}
        task['poller']['suffix'] = suffix
        task['poller']['metric'] = metric
        task['poller']['attribute'] = attribute

    success = ocp_common.delete_workflow(cluster_names, 'iotel', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)