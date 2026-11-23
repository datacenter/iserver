import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("mtv")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'provider', 'nmap', 'smap', 'plan', 'run'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="Forklift Controller CRD")
@click.option("--provider", default='', callback=validations.empty_string_to_none, help="Provider name")
@click.option("--vc-url", default='', callback=validations.empty_string_to_none, help="vCenter URL")
@click.option("--vc-user", default='', callback=validations.empty_string_to_none, help="vCenter username")
@click.option("--vc-pass", default='', callback=validations.empty_string_to_none, help="vCenter password")
@click.option("--vc-ssl", is_flag=True, show_default=True, default=False, help="vCenter SSL verify")
@click.option("--vddk", default='', callback=validations.empty_string_to_none, help="vddk init image url")
@click.option("--plan", default='', callback=validations.empty_string_to_none, help="Plan name")
@click.option("--nmap", default='', callback=validations.empty_string_to_none, help="Network map name")
@click.option("--smap", default='', callback=validations.empty_string_to_none, help="Storage map name")
@click.option("--source", multiple=True, help="Map source")
@click.option("--destination", multiple=True, help="Map destination")
@click.option("--vm", "vms", multiple=True, help="Virtual machine name")
@click.option("--type", "migration_type", type=click.Choice(['cold', 'warm'], case_sensitive=False), default='cold', show_default=True, help="Migration type")
@click.option("--target", default='default', callback=validations.empty_string_to_none, show_default=True, help="Target namespace")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_mtv_command(ctx, cluster_names, mode, channel, filename, provider, vc_url, vc_user, vc_pass, vc_ssl, vddk, plan, nmap, smap, source, destination, vms, migration_type, target, no_wait, no_confirm):
    """Set mtv operator in openshift cluster"""

    task = {}

    if mode in ['operator']:
        task['operator'] = {}
        task['operator']['channel'] = channel

    if mode in ['instance']:
        task['instance'] = {}
        task['instance']['filename'] = filename

    if mode in ['provider']:
        task['provider'] = {}
        task['provider']['provider'] = provider
        task['provider']['vc-url'] = vc_url
        task['provider']['vc-user'] = vc_user
        task['provider']['vc-pass'] = vc_pass
        task['provider']['vc-ssl'] = vc_ssl
        task['provider']['vddk'] = vddk

    if mode in ['nmap']:
        if len(source) == 0:
            ctx.my_output.error('Source network required')
            sys.exit(1)
        
        if len(destination) == 0:
            ctx.my_output.error('Destination network required')
            sys.exit(1)

        if len(source) != len(destination):
            ctx.my_output.error('Source and destination network count must be the same')
            sys.exit(1)

        task['nmap'] = {}
        task['nmap']['map'] = nmap
        task['nmap']['source'] = provider
        task['nmap']['destination'] = 'host'
        task['nmap']['network'] = []
        for index in range(0, len(source)):
            network = {}
            network['source'] = source[index]
            network['destination'] = destination[index]
            task['nmap']['network'].append(network)

    if mode in ['smap']:
        if len(source) == 0:
            ctx.my_output.error('Source storage required')
            sys.exit(1)
        
        if len(destination) == 0:
            ctx.my_output.error('Destination storage required')
            sys.exit(1)

        if len(source) != len(destination):
            ctx.my_output.error('Source and destination storage count must be the same')
            sys.exit(1)

        task['smap'] = {}
        task['smap']['map'] = smap
        task['smap']['source'] = provider
        task['smap']['destination'] = 'host'
        task['smap']['storage'] = []
        for index in range(0, len(source)):
            storage = {}
            storage['source'] = source[index]
            storage['destination'] = destination[index]
            task['smap']['storage'].append(storage)

    if mode in ['plan']:
        task['plan'] = {}
        task['plan']['plan'] = plan
        task['plan']['source'] = provider
        task['plan']['destination'] = 'host'
        task['plan']['network'] = nmap
        task['plan']['storage'] = smap
        task['plan']['vm'] = vms
        task['plan']['type'] = migration_type
        task['plan']['target'] = target

    if mode in ['run']:
        task['run'] = {}
        task['run']['action'] = 'run'
        task['run']['plan'] = plan
        task['run']['wait'] = not no_wait

    success = ocp_common.set_workflow(cluster_names, 'mtv', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)