import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("ai")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="DataScienceCluster CRD")
@click.option("--mode", type=click.Choice(['operator', 'cluster', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_ai_command(ctx, cluster_names, channel, filename, mode, no_confirm):
    """Set data science (ai) operator in openshift cluster"""

    task = {}

    if mode in ['operator', 'all']:
        task['operator'] = {}
        task['operator']['channel'] = channel

    if mode in ['cluster', 'all']:
        task['cluster'] = {}
        task['cluster']['filename'] = filename

    success = ocp_common.set_workflow(cluster_names, 'ai', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)