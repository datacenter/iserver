import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("odf")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'cluster', 'all'], case_sensitive=False), default='operator', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="ODF Cluster")
@click.option("--sc", "storage_class", default='odf-sc', callback=validations.empty_string_to_none, show_default=True, help="Storage class name")
@click.option("--replica", default=0, type=click.INT, show_default=True, help="Replica")
@click.option("--count", default=0, type=click.INT, show_default=True, help="Count")
@click.option("--default-sc", is_flag=True, show_default=True, default=False, help="Set ODF storage class as default")
@click.option("--nfs", is_flag=True, show_default=True, default=False, help="Enable nfs")
@click.option("--flexible", is_flag=True, show_default=True, default=False, help="Flexible scaling")
@click.option("--tools", is_flag=True, show_default=True, default=False, help="Ceph tools")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_odf_command(
        ctx, 
        cluster_names, 
        mode, 
        channel, 
        filename,
        storage_class,
        replica,
        count,
        default_sc,
        nfs,
        flexible,
        tools,
        no_confirm
    ):
    """Set openshift data foundation operator in openshift cluster"""

    task = {}

    if mode in ['operator', 'all']:
        task['operator'] = {}
        task['operator']['channel'] = channel

    if mode in ['cluster', 'all']:
        task['cluster'] = {}
        task['cluster']['filename'] = filename
        task['cluster']['sc'] = storage_class
        task['cluster']['replica'] = replica
        task['cluster']['count'] = count
        task['cluster']['default_sc'] = default_sc
        task['cluster']['nfs'] = nfs
        task['cluster']['flexible'] = flexible
        task['cluster']['tools'] = tools

    success = ocp_common.set_workflow(cluster_names, 'odf', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)