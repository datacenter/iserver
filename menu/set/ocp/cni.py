import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("cni")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['cilium'], case_sensitive=False), default='', show_default=True, help="Target cni")
@click.option("--cidr", default='', callback=validations.validate_ip_subnet, help="Target cidr")
@click.option("--host-prefix", default=24, type=click.INT, show_default=True, help="Target host prefix")
@click.option("--manifest", default='', callback=validations.validate_directory, help="Manifest directory")
@click.option("--start", default=1, type=click.INT, show_default=True, help="Starting step")
@click.option("--stop", default=10, type=click.INT, show_default=True, help="Ending step")
@click.option("--no-reload", is_flag=True, show_default=True, default=False, help="Disable auto-reload in case of failed mcp-triggered restart")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cni_command(
        ctx, 
        cluster_names, 
        mode,
        cidr,
        host_prefix,
        manifest,
        start,
        stop,
        no_reload,
        no_confirm
    ):
    """Set openshift data foundation operator in openshift cluster"""

    task = {}

    if mode in ['cilium']:
        task['migrate'] = {}
        task['migrate']['cidr'] = cidr
        task['migrate']['host_prefix'] = host_prefix
        task['migrate']['manifest'] = manifest
        task['migrate']['start'] = start
        task['migrate']['stop'] = stop
        task['migrate']['reload'] = not no_reload
        
    success = ocp_common.set_workflow(cluster_names, 'cni', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)