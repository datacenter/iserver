import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("bgp")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature', 'crd', 'wipe'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--filename", default='', callback=validations.empty_string_to_none, help="CRD filename")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cilium_bgp_command(
        ctx, 
        cluster_names, 
        mode, 
        filename,
        no_confirm
    ):
    """Delete cilium bgp control plane"""

    task = {}
    if mode in ['crd']:
        task['crd'] = {}
        task['crd']['filename'] = filename

    if mode in ['feature']:
        task['feature'] = {}

    if mode in ['wipe', 'feature']:
        task['wipe'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'cilium-bgp', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)