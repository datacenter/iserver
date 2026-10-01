import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("service-mesh")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--mode", type=click.Choice(['operator'], case_sensitive=False), default='operator', show_default=True, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_service_mesh_command(ctx, cluster_names, channel, mode, no_confirm):
    """Set service_mesh operator in openshift cluster"""

    task = {}

    if mode in ['operator', 'all']:
        task['operator'] = {}
        task['operator']['channel'] = channel

    success = ocp_common.set_workflow(cluster_names, 'service-mesh', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)