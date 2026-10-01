import sys
import click
from menu import validations
from lib.workflow import ocp_common

@click.command("vast")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'driver', 'cluster', 'storage', 'wipe', 'all'], case_sensitive=False), callback=validations.validate_option, help="Mode of operation")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="VAST CSI CRD")
@click.option("--name", default='', callback=validations.empty_string_to_none, show_default=True, help="CRD name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_vast_command(ctx, cluster_names, mode, filename, name, no_confirm):
    """Delete vast operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}

    if mode in ['driver', 'all']:
        task['driver'] = {}
        task['driver']['filename'] = filename
        task['driver']['name'] = name

    if mode in ['cluster', 'all']:
        task['cluster'] = {}
        task['cluster']['filename'] = filename
        task['cluster']['name'] = name

    if mode in ['storage', 'all']:
        task['storage'] = {}
        task['storage']['filename'] = filename
        task['storage']['name'] = name
    
    if mode in ['wipe', 'all']:
        task['wipe'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'vast', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)