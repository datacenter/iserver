import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("inb")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--ip", default='', callback=validations.validate_ip, help="Inb ip address")
@click.option("--username", default='', callback=validations.empty_string_to_none, help="Inb ssh username")
@click.option("--password", default='', callback=validations.empty_string_to_none, help="Inb ssh password")
@click.option("--mesh-id", default=0, type=click.INT, help="Cluster mesh id")
@click.option("--mesh-name", default='', callback=validations.empty_string_to_none, help="Cluster mesh name")
@click.option("--mesh-port", default=0, help="Cluster mesh port")
@click.option("--cidr", default='', callback=validations.validate_ip_subnet, help="POD cidr")
@click.option("--pnet", default='', callback=validations.empty_string_to_none, help="Private network name")
@click.option("--nic", default='', callback=validations.empty_string_to_none, help="VM network interface name")
@click.option("--gateway", default='', callback=validations.validate_ip_subnet, help="VM network gateway")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_inb_command(ctx, cluster_names, mode, ip, username, password, mesh_id, mesh_name, mesh_port, cidr, pnet, nic, gateway, no_confirm):
    """Set isovalent network bridge"""

    task = {}
    if mode in ['feature']:
        task['feature'] = {}
        task['feature']['ip'] = ip
        task['feature']['username'] = username
        task['feature']['password'] = password
        task['feature']['mesh-id'] = mesh_id
        task['feature']['mesh-name'] = mesh_name
        task['feature']['mesh-port'] = mesh_port
        task['feature']['cidr'] = cidr
        task['feature']['pnet'] = pnet
        task['feature']['nic'] = nic
        task['feature']['gateway'] = gateway

    success = ocp_common.set_workflow(cluster_names, 'cilium-inb', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)