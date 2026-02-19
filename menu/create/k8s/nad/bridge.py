import sys
import traceback
import click
from menu import user_inputs
from menu import validations
from lib.workflow.k8s import nad_bridge_create as workflow

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("bridge")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Name")
@click.option("--bridge", default='', callback=validations.empty_string_to_none, help="Bridge name")
@click.option("--ipam", type=click.Choice(['static', 'local'], case_sensitive=False), default='static', show_default=True, help="IPAM mode")
@click.option("--address", default='', callback=validations.empty_string_to_none, help="Address")
@click.option("--gateway", default='', callback=validations.empty_string_to_none, help="Gateway CIDR")
@click.option("--route", multiple=True, help="Route")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def create_k8s_nad_bridge_command(
        ctx,
        cluster_name,
        namespace,
        name,
        bridge,
        ipam,
        address,
        gateway,
        route,
        no_confirm
        ):
    """Create k8s nad ipvlan"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        interactive = False

        if namespace is None:
            namespace = user_inputs.get_value(ctx, 'NAD Namespace')
            interactive = True

        if name is None:
            name = user_inputs.get_value(ctx, 'NAD Name')
            interactive = True

        if bridge is None:
            if interactive:
                bridge = user_inputs.get_value(ctx, 'Bridge name')
            else:
                bridge = name
        
        if ipam == 'static':
            if address is None:
                address = user_inputs.get_ip_address(ctx, '[IPAM static] IPv4 address')
                interactive = True

        if ipam == 'local':
            if address is None:
                start = user_inputs.get_ip_address(ctx, '[IPAM host-local] IPv4 address start')
                end = user_inputs.get_ip_address(ctx, '[IPAM host-local]IPv4 address end')
                address = '%s-%s' % (start, end)
                interactive = True

        if gateway is None:
            gateway = user_inputs.get_cidr(ctx, 'IPv4 gateway cidr')
            interactive = True

        if len(route) == 0 and interactive:
            route = []
            while True:
                dst = user_inputs.get_cidr(ctx, 'Route subnet', empty=True)
                if len(dst) == 0:
                    break

                route.append(dst)

        params = {}
        params['cluster'] = cluster_name
        params['namespace'] = namespace
        params['name'] = name
        params['bridge'] = bridge
        params['ipam'] = ipam
        params['address'] = address
        params['gateway'] = gateway
        params['route'] = []
        for item in route:
            params['route'].append(item)
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
