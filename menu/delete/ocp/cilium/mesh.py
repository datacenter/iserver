import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("mesh")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature', 'cluster', 'timescape'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--mesh-name", default='', callback=validations.empty_string_to_none, help="Cluster mesh name")
@click.option("--mesh-ip", default='', callback=validations.validate_ip, help="Cluster mesh ip")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cilium_mesh_command(ctx, cluster_names, mode, mesh_name, mesh_ip, no_confirm):
    """Delete cilium cluster mesh"""

    task = {}
    if mode in ['feature']:
        task['feature'] = {}

    if mode in ['cluster']:
        task['cluster'] = {}
        task['cluster']['mesh-name'] = mesh_name
        task['cluster']['mesh-ip'] = mesh_ip

    if mode in ['timescape']:
        task['timescape'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'cilium-mesh', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)