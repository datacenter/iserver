import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("inb")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--mesh-name", default='', callback=validations.empty_string_to_none, help="Cluster mesh name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cilium_inb_command(ctx, cluster_names, mode, mesh_name, no_confirm):
    """Delete isovalent network bridge"""

    task = {}
    if mode in ['feature']:
        task['feature'] = {}
        task['feature']['mesh-name'] = mesh_name

    success = ocp_common.delete_workflow(cluster_names, 'cilium-inb', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)