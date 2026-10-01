import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("bgp")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature', 'crd'], case_sensitive=False), default='', help="Mode of operation")
@click.option("--filename", default='', callback=validations.empty_string_to_none, help="CRD filename")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_bgp_command(
        ctx, 
        cluster_names, 
        mode, 
        filename,
        no_confirm
    ):
    """Set cilium bgp control plane"""

    task = {}
    if mode in ['feature']:
        task['feature'] = {}

    if mode in ['crd']:
        task['crd'] = {}
        task['crd']['filename'] = filename

    success = ocp_common.set_workflow(cluster_names, 'cilium-bgp', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)