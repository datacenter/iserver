import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("pod")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Name")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_k8s_pod_command(
        ctx,
        cluster_names,
        namespace,
        name,
        no_wait,
        no_confirm
        ):
    """Delete k8s pod"""

    task = {}
    task['pod'] = {}
    task['pod']['namespace'] = namespace
    task['pod']['name'] = name
    task['pod']['wait'] = not no_wait

    success = ocp_common.delete_workflow(cluster_names, 'ocp-pod', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)