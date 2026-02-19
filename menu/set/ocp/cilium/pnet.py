import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_pnet import feature_enable
from lib.workflow.ocp_cilium_pnet import network_create
from lib.workflow.ocp_cilium_pnet import pod_create
from lib.workflow.ocp_cilium_pnet import webhook_enable
from lib.workflow.ocp_cilium_pnet import test


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("pnet")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['feature', 'webhook', 'network', 'pod', 'test'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--fixup", is_flag=True, show_default=True, default=False, help="Fixup private network enablement")
@click.option("--network", default='', callback=validations.empty_string_to_none, help="Private network name")
@click.option("--subnet", default='', callback=validations.empty_string_to_none, help="Network subnet")
@click.option("--gateway", default='', callback=validations.empty_string_to_none, help="Network gateway")
@click.option("--inb", multiple=True, help="Network bridge")
@click.option("--namespace", default='default', callback=validations.empty_string_to_none, help="Pod/vm namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Pod/vm name")
@click.option("--image", type=click.Choice(['netshoot'], case_sensitive=False), default='netshoot', show_default=True, help="Pod/vm image")
@click.option("--ipv4", "ipv4_address", default='', callback=validations.empty_string_to_none, help="Pod/vm ip v4")
@click.option("--mac", "mac_address", default='', callback=validations.empty_string_to_none, help="Pod/vm mac")
@click.option("--no-cleanup", is_flag=True, show_default=True, default=False, help="Leave test resources")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_pnet_command(
        ctx, 
        cluster_name, 
        mode, 
        fixup, 
        network, 
        subnet,
        gateway,
        inb,
        namespace, 
        name, 
        image, 
        ipv4_address, 
        mac_address, 
        no_cleanup, 
        no_confirm
    ):
    """Set cilium private networking"""

    try:
        if mode in ['feature']:
            params = {}
            params['cluster'] = cluster_name
            params['fixup'] = fixup
            params['confirmation'] = not no_confirm

            success = feature_enable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['webhook']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm

            success = webhook_enable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['network']:
            params = {}
            params['cluster'] = cluster_name
            params['network'] = network
            params['subnet'] = subnet
            params['gateway'] = gateway
            params['inb'] = []
            for item in inb:
                params['inb'].append(item)
            params['confirmation'] = not no_confirm

            success = network_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit  
                        
        if mode in ['pod']:
            params = {}
            params['cluster'] = cluster_name
            params['network'] = network
            params['app-namespace'] = namespace
            params['app-name'] = name
            params['app-image'] = image
            params['app-ipv4'] = ipv4_address
            params['app-mac'] = mac_address
            params['confirmation'] = not no_confirm

            success = pod_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit  
                        
        if mode in ['test']:
            params = {}
            params['cluster'] = cluster_name
            params['cleanup'] = not no_cleanup
            params['confirmation'] = not no_confirm

            success = test.run(
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
