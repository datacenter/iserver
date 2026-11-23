import sys
import traceback
import click
from menu import user_inputs
from menu import validations
from lib.workflow.k8s import nad_vlan_create as workflow

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("vlan")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Name")
@click.option("--master", default='', callback=validations.empty_string_to_none, help="Master interface")
@click.option("--vlan", type=click.INT, default=0, help="VLAN ID")
@click.option("--ipam", type=click.Choice(['dhcp', 'static', 'local'], case_sensitive=False), default='dhcp', show_default=True, help="IPAM mode")
@click.option("--address", default='', callback=validations.empty_string_to_none, help="Address")
@click.option("--gateway", default='', callback=validations.empty_string_to_none, help="Gateway CIDR")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def create_k8s_nad_vlan_command(
        ctx,
        cluster_name,
        namespace,
        name,
        master,
        vlan,
        ipam,
        address,
        gateway,
        no_confirm
        ):
    """Create k8s nad vlan"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        if namespace is None:
            namespace = user_inputs.get_value(ctx, 'NAD Namespace')

        if name is None:
            name = user_inputs.get_value(ctx, 'NAD Name')

        if master is None:
            master = user_inputs.get_value(ctx, 'Master interface name')

        if vlan == 0:
            vlan = user_inputs.get_integer(ctx, 'VLAN ID', min_value=1, max_value=4096)
        
        if ipam == 'dhcp':
            address = None
            gateway = None
            
        if ipam == 'static':
            if address is None:
                address = user_inputs.get_ip_address(ctx, 'IPv4 address')

            if gateway is None:
                gateway = user_inputs.get_cidr(ctx, 'IPv4 gateway cidr')

        if ipam == 'local':
            if address is None:
                start = user_inputs.get_ip_address(ctx, 'IPv4 address start')
                end = user_inputs.get_ip_address(ctx, 'IPv4 address end')
                address = '%s-%s' % (start, end)

            if gateway is None:
                gateway = user_inputs.get_cidr(ctx, 'IPv4 gateway cidr')

        params = {}
        params['cluster'] = cluster_name
        params['namespace'] = namespace
        params['name'] = name
        params['master'] = master
        params['vlan'] = vlan
        params['ipam'] = ipam
        params['address'] = address
        params['gateway'] = gateway
        params['confirmation'] = not no_confirm

        success = workflow.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit
        
    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
