import os
import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("nfs")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--url", default='', callback=validations.empty_string_to_none, help="Helm chart url")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Helm chart namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Helm chart name")
@click.option("--version", default='', callback=validations.empty_string_to_none, help="Helm chart version")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_nfs_command(
        ctx,
        cluster_names,
        url,
        namespace,
        name,
        version,
        no_confirm
        ):
    """Set ocp cluster nfs"""

    task = {}
    task['feature'] = {}
    task['feature']['helm_repo'] = url
    task['feature']['helm_namespace'] = namespace
    task['feature']['helm_name'] = name
    task['feature']['helm_version'] = version

    success = ocp_common.set_workflow(cluster_names, 'nfs', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)