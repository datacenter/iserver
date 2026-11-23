import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("vm")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--namespace", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="Virtual machine namespace")
@click.option("--name", default='', show_default=False, callback=validations.empty_string_to_none, help="Virtual machine name")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="No wait")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_vm_command(
        ctx,
        cluster_names,
        namespace,
        name,
        no_wait,
        no_confirm
        ):
    """Delete vm"""

    task = {}
    task['delete'] = {}
    task['delete']['namespace'] = namespace
    task['delete']['name'] = name

    success = ocp_common.delete_workflow(cluster_names, 'ocp-vm', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)