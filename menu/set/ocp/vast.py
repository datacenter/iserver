import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("vast")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'driver', 'cluster', 'storage'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="VAST CSI CRD")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_vast_command(
        ctx, 
        cluster_names, 
        mode,
        channel,
        filename,
        no_confirm
    ):
    """Set vast csi operator in openshift cluster"""

    task = {}
    if mode == 'operator':
        task['operator'] = {}
        task['operator']['channel'] = channel

    if mode == 'driver':
        task['driver'] = {}
        task['driver']['filename'] = filename

    if mode == 'cluster':
        task['cluster'] = {}
        task['cluster']['filename'] = filename

    if mode == 'storage':
        task['storage'] = {}
        task['storage']['filename'] = filename

    success = ocp_common.set_workflow(cluster_names, 'vast', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)