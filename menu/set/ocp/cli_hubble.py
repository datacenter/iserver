import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("cli-hubble")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--url", default='', callback=validations.empty_string_to_none, help="Hubble download url")
@click.option("--version", default='', callback=validations.empty_string_to_none, help="Hubble version")
@click.option("--overwrite", is_flag=True, show_default=True, default=False, help="Overwrite if exists")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cli_hubble(
        ctx,
        cluster_names,
        url,
        version,
        overwrite,
        no_confirm
        ):
    """Set ocp cluster hubble"""

    task = {}
    task['hubble'] = {}
    task['hubble']['url'] = url
    task['hubble']['version'] = version
    task['hubble']['overwrite'] = overwrite

    success = ocp_common.set_workflow(cluster_names, 'cli', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)