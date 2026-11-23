import sys
import click
from menu import validations
from lib.workflow.ocp_cilium_inb import get


@click.command("inb")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--vc", "vcenter", default='', callback=validations.validate_vc_name, help="vCenter name")
@click.option("--mesh-name", default='', callback=validations.empty_string_to_none, help="Cluster mesh name")
@click.option("--view", "-v", default=['all'], help="[ssh|vc|kube|pnet|mesh|all]", show_default=True, multiple=True)
def get_ocp_cilium_inb_command(ctx, cluster_names, vcenter, mesh_name, view):
    """Get isovalent network bridge"""

    params = {}
    params['cluster'] = cluster_names
    params['vcenter'] = vcenter
    params['mesh-name'] = mesh_name
    params['view'] = view
    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)