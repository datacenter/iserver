import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("nmstate")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'lldp', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="NMState CRD")
@click.option("--node", default='', callback=validations.empty_string_to_none, show_default=True, help="Node name")
@click.option("--fw", is_flag=True, show_default=True, default=False, help="Disable LLDP on NIC fw level")
@click.option("--delete-nncp", is_flag=True, show_default=True, default=False, help="Delete NNCP")
@click.option("--with-down", is_flag=True, show_default=True, default=False, help="Include interfaces in down state")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_nmstate_command(
        ctx,
        cluster_names,
        mode,
        channel,
        filename,
        node, 
        fw,
        delete_nncp,
        with_down,
        no_confirm
    ):
    """Set nmstate operator in openshift cluster"""

    task = {}

    if mode in ['operator', 'all']:
        task['operator'] = {}
        task['operator']['channel'] = channel

    if mode in ['instance', 'all']:
        task['instance'] = {}
        task['instance']['filename'] = filename

    if mode in ['lldp', 'all']:
        task['lldp'] = {}
        task['lldp']['enable'] = True
        task['lldp']['node'] = node
        task['lldp']['fw'] = fw
        task['lldp']['delete-nncp'] = delete_nncp
        task['lldp']['include-down'] = with_down

    success = ocp_common.set_workflow(cluster_names, 'nmstate', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)