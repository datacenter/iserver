import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("image")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--url", default='', callback=validations.empty_string_to_none, help="Image url")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_image_command(ctx, cluster_names, url, no_confirm):
    """Set cilium cni image"""

    task = {}
    task['image'] = {}
    task['image']['url'] = url

    success = ocp_common.set_workflow(cluster_names, 'cilium', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)