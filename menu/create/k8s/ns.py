import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("ns")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Namespace name")
@click.option("--label", multiple=True, help="Label")
@click.option("--kubemacpool", is_flag=True, show_default=True, default=False, help="Kubemac pool label")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def create_k8s_ns_command(
        ctx,
        cluster_names,
        name,
        label,
        kubemacpool,
        no_confirm
        ):
    """Create k8s vm"""

    task = {}
    task['ns'] = {}
    task['ns']['namespace'] = name
    task['ns']['labels'] = {}
    
    for item in label:
        if len(item.split('=')) != 2:
            ctx.my_output.error('Label must be in key=value format')
            sys.exit(1)

        task['ns']['labels'][item.split('=')[0]] = item.split('=')[1]
        
    if kubemacpool:
        task['ns']['labels']['mutatevirtualmachines.kubemacpool.io'] = 'ignore'

    success = ocp_common.set_workflow(cluster_names, 'k8s', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)