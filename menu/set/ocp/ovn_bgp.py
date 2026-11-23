import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("ovn-bgp")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature', 'ra', 'all', 'config', 'ra-config'], case_sensitive=False), default='feature', show_default=True, help="Mode of operation")
@click.option("--config", default='', callback=validations.empty_string_to_none, show_default=True, help="FRR configuration filename")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_ovn_bgp(
        ctx,
        cluster_names,
        mode,
        config,
        no_confirm
        ):
    """Set ocp cluster ovn bgp"""

    task = {}

    if mode in ['feature', 'all']:
        task['feature'] = {}
        task['feature']['mode'] = mode

    if mode in ['ra', 'all']:
        task['ra'] = {}
        task['ra']['mode'] = mode

    if mode in ['config']:
        task['config'] = {}
        task['config']['config'] = config

    if mode in ['ra-config']:
        task['ra-config'] = {}
        task['ra-config']['config'] = config

    success = ocp_common.set_workflow(cluster_names, 'ovn-bgp', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)