import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("pnet")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature', 'network', 'pod', 'test'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--option", default=[], help="multus, local-access, net-binding, webhook, certmanager", show_default=True, multiple=True)
@click.option("--option-mode", type=click.Choice(['set', 'add'], case_sensitive=False), default='add', show_default=True, help="Private network option mode")
# @click.option("--pnet", type=click.Choice(['default', 'bridge', 'local-access'], case_sensitive=False), default='default', show_default=True, help="Private network mode")
# @click.option("--network", default='', callback=validations.empty_string_to_none, help="Private network name")
# @click.option("--cidr4", multiple=True, help="Subnet cidrv4")
# @click.option("--cidr6", multiple=True, help="Subnet cidrv6")
# @click.option("--nad", multiple=True, help="Multus enablement")
# @click.option("--inb", multiple=True, help="Network bridge")
# @click.option("--namespace", default='default', callback=validations.empty_string_to_none, help="Pod/vm namespace")
# @click.option("--name", default='', callback=validations.empty_string_to_none, help="Pod/vm name")
# @click.option("--image", type=click.Choice(['netshoot'], case_sensitive=False), default='netshoot', show_default=True, help="Pod/vm image")
# @click.option("--ipv4", "ipv4_address", default='', callback=validations.empty_string_to_none, help="Pod/vm ip v4")
# @click.option("--mac", "mac_address", default='', callback=validations.empty_string_to_none, help="Pod/vm mac")
# @click.option("--no-cleanup", is_flag=True, show_default=True, default=False, help="Leave test resources")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_pnet_command(
        ctx, 
        cluster_names, 
        mode, 
        option,
        option_mode,
        # pnet,
        # network,
        # cidr4,
        # cidr6,
        # nad,
        # inb,
        # namespace, 
        # name, 
        # image, 
        # ipv4_address, 
        # mac_address, 
        # no_cleanup, 
        no_confirm
    ):
    """Set cilium private network"""

    task = {}

    if mode in ['feature']:
        task['feature'] = {}
        task['feature']['option'] = option
        task['feature']['option-mode'] = option_mode
        # task['feature']['mode'] = pnet

    # if mode in ['multus']:
    #     task['multus'] = {}

    # if mode in ['webhook']:
    #     task['webhook'] = {}

    # if mode in ['network']:
    #     task['network'] = {}
    #     task['network']['name'] = network
    #     task['network']['cidrv4'] = cidr4
    #     task['network']['cidrv6'] = cidr6
    #     task['network']['nad'] = nad
        # task['network']['inb'] = inb

    # if mode in ['pod']:
    #     task['pod'] = {}
    #     task['pod']['network'] = network
    #     task['pod']['app-namespace'] = namespace
    #     task['pod']['app-name'] = name
    #     task['pod']['app-image'] = image
    #     task['pod']['app-ipv4'] = ipv4_address
    #     task['pod']['app-mac'] = mac_address

    # if mode in ['test']:
    #     task['test'] = {}
    #     task['test']['cleanup'] = not no_cleanup

    success = ocp_common.set_workflow(cluster_names, 'cilium-pnet', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)