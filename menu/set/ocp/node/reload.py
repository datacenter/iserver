import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("reload")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--node", multiple=True, help="Node name")
@click.option("--no-pre", is_flag=True, show_default=True, default=False, help="Skip pre checks")
@click.option("--no-post", is_flag=True, show_default=True, default=False, help="Skip post checks")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode in case of eviction problems")
def set_ocp_node_reload_command(
        ctx,
        cluster_names,
        node,
        no_pre,
        no_post,
        no_confirm
        ):
    """Set k8s node graceful reboot (reload)"""

    task = {}
    task['reload'] = {}
    task['reload']['node'] = node
    task['reload']['pre'] = not no_pre
    task['reload']['post'] = not no_post

    success = ocp_common.set_workflow(cluster_names, 'ocp-node', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)