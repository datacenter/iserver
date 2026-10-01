import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("mesh")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature', 'cluster', 'timescape'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--mesh-id", default=0, type=click.INT, help="Cluster mesh id")
@click.option("--mesh-name", default='', callback=validations.empty_string_to_none, help="Cluster mesh name")
@click.option("--mesh-ip", default='', callback=validations.validate_ip, help="Cluster mesh ip address")
@click.option("--mesh-port", type=click.INT, help="Cluster mesh port")
@click.option("--ca-crt", default='', callback=validations.empty_string_to_none, show_default=True, help="Root ca crt")
@click.option("--ca-key", default='', callback=validations.empty_string_to_none, show_default=True, help="Root ca key")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="No-wait for cluster mesh up")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_mesh_command(ctx, cluster_names, mode, mesh_id, mesh_name, mesh_ip, mesh_port, ca_crt, ca_key, no_wait, no_confirm):
    """Set cilium cluster mesh"""

    task = {}
    if mode in ['feature']:
        task['feature'] = {}
        task['feature']['mesh-id'] = mesh_id
        task['feature']['mesh-name'] = mesh_name
        task['feature']['mesh-port'] = mesh_port
        task['feature']['ca-crt'] = ca_crt
        task['feature']['ca-key'] = ca_key

    if mode in ['cluster']:
        task['cluster'] = {}
        task['cluster']['mesh-name'] = mesh_name
        task['cluster']['mesh-ip'] = mesh_ip
        task['cluster']['mesh-port'] = mesh_port
        task['cluster']['wait'] = not no_wait

    if mode in ['timescape']:
        task['timescape'] = {}

    success = ocp_common.set_workflow(cluster_names, 'cilium-mesh', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)