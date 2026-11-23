import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("ssh")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--role", "node_role", type=click.Choice(['any', 'master', 'worker'], case_sensitive=False), default='any', show_default=True)
@click.option("--filename", multiple=True, help="SSH public key to be deleted")
@click.option("--key", multiple=True, help="SSH public key search pattern to be removed")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="No-wait for mcp update")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_ssh_command(
        ctx,
        cluster_names,
        node_role,
        filename,
        key,
        no_wait,
        no_confirm
        ):
    """Delete ocp ssh authorized keys"""

    task = {}
    task['key'] = {}
    task['key']['role'] = node_role
    task['key']['filename'] = filename
    task['key']['key'] = key
    task['key']['wait'] = not no_wait

    success = ocp_common.delete_workflow(cluster_names, 'ssh', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)