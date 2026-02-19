import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_inb import feature_enable


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("inb")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
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
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_inb_command(ctx, cluster_name, mode, ip, username, password, mesh_id, mesh_name, mesh_port, cidr, pnet, nic, gateway, verbose, no_confirm):
    """Set isovalent network bridge"""

    try:
        if mode in ['feature']:
            params = {}
            params['cluster'] = cluster_name
            params['ip'] = ip
            params['username'] = username
            params['password'] = password
            params['mesh-id'] = mesh_id
            params['mesh-name'] = mesh_name
            params['mesh-port'] = mesh_port
            params['cidr'] = cidr
            params['pnet'] = pnet
            params['nic'] = nic
            params['gateway'] = gateway
            params['verbose'] = verbose
            params['confirmation'] = not no_confirm

            success = feature_enable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit         
            
    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
