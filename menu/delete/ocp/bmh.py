import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("bmh")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['node'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--node", default='', callback=validations.empty_string_to_none, show_default=True, help="Host name")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_bmh_command(ctx, cluster_names, mode, node, no_wait, no_confirm):
    """Set bare metal host in openshift cluster"""

    task = {}
    if mode in ['node']:
        task['node'] = {}
        task['node']['node'] = node
        task['node']['wait'] = not no_wait

    success = ocp_common.delete_workflow(cluster_names, 'bmh', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)