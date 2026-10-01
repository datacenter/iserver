import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("file")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, show_default=True, help="Namespace name")
@click.option("--filename", multiple=True, help="YAML crds filename")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_file_command(
        ctx, 
        cluster_names, 
        namespace,
        filename,
        no_confirm
    ):
    """Delete openshift crds from file(s)"""

    task = {}
    task['file'] = {}
    task['file']['namespace'] = namespace
    task['file']['filename'] = filename

    success = ocp_common.delete_workflow(cluster_names, 'cli', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)