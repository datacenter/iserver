import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("portworx")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'cluster', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_portworx_command(ctx, cluster_names, mode, channel, no_confirm):
    """Set portworx operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}
        task['operator']['channel'] = channel

    success = ocp_common.set_workflow(cluster_names, 'portworx', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)