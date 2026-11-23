import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("minio")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator'], case_sensitive=False), default='operator', show_default=True, help="Mode of operation")
@click.option("--wipe", is_flag=True, default=False, help="Wipe crds")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_minio_command(ctx, cluster_names, mode, wipe, no_confirm):
    """Delete minio operator in openshift cluster"""

    task = {}
    if mode in ['operator']:
        task['operator'] = {}
        task['operator']['wipe'] = wipe

    success = ocp_common.delete_workflow(cluster_names, 'minio', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)