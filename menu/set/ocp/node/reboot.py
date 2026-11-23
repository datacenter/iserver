import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("reboot")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--node", multiple=True, help="Node name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_node_reboot_command(
        ctx,
        cluster_names,
        node,
        no_confirm
        ):
    """Set k8s node reboot"""

    task = {}
    task['reboot'] = {}
    task['reboot']['node'] = node

    success = ocp_common.set_workflow(cluster_names, 'ocp-node', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)