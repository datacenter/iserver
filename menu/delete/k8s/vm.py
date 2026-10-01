import sys
import click
from lib.workflow import ocp_common
from menu import validations


class ErrorExit(Exception):
    pass


@click.command("vm")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_k8s_vm_command(
        ctx,
        cluster_names,
        namespace,
        name,
        no_wait,
        no_confirm
        ):
    """Delete k8s vm"""

    task = {}
    task['vm'] = {}
    task['vm']['namespace'] = namespace
    task['vm']['name'] = name
    task['vm']['wait'] = not no_wait

    success = ocp_common.delete_workflow(cluster_names, 'ocp-vm', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)