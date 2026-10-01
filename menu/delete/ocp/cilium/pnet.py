import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("pnet")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature', 'webhook', 'network', 'wipe'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--network", default='', callback=validations.empty_string_to_none, help="Private network name")
@click.option("--wipe", "wipe_option", is_flag=True, default=False, help="Wipe crds")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cilium_pnet_command(ctx, cluster_names, mode, network, wipe_option, no_confirm):
    """Delete cilium cluster private network"""

    task = {}
    if mode in ['feature']:
        task['feature'] = {}
        task['feature']['wipe'] = wipe_option

    if mode in ['webhook']:
        task['webhook'] = {}

    if mode in ['network']:
        task['network'] = {}
        task['network']['name'] = network

    if mode in ['wipe']:
        task['wipe'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'cilium-pnet', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)