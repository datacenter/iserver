import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("cli-helm")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--url", default='', callback=validations.empty_string_to_none, help="Helm download url")
@click.option("--version", default='', callback=validations.empty_string_to_none, help="Helm version")
@click.option("--overwrite", is_flag=True, show_default=True, default=False, help="Overwrite if exists")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cli_helm(
        ctx,
        cluster_names,
        url,
        version,
        overwrite,
        no_confirm
        ):
    """Set ocp cluster helm"""


    task = {}
    task['helm'] = {}
    task['helm']['url'] = url
    task['helm']['version'] = version
    task['helm']['overwrite'] = overwrite

    success = ocp_common.set_workflow(cluster_names, 'cli', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)