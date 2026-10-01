import sys
import click
from lib.workflow import ocp_common
from menu import validations
from menu import user_inputs


@click.command("ssh")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--role", "node_role", type=click.Choice(['any', 'master', 'worker'], case_sensitive=False), default='any', show_default=True)
@click.option("--filename", multiple=True, help="SSH public key to be added")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="No-wait for mcp update")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_ssh_command(
        ctx,
        cluster_names,
        node_role,
        filename,
        no_wait,
        no_confirm
        ):
    """Set ocp ssh authorized keys"""

    if len(filename) == 0:
        item = user_inputs.get_value(ctx, prompt='SSH public key location')
        if len(item) == 0:
            sys.exit(1)
        
        filename = [item]

    task = {}
    task['key'] = {}
    task['key']['role'] = node_role
    task['key']['filename'] = filename
    task['key']['wait'] = not no_wait

    success = ocp_common.set_workflow(cluster_names, 'ssh', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)