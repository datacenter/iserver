import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_mtv_operator import operator_create
from lib.workflow.ocp_mtv_operator import instance_create
from lib.workflow.ocp_mtv_operator import provider_create
from lib.workflow.ocp_mtv_operator import network_map_create
from lib.workflow.ocp_mtv_operator import storage_map_create
from lib.workflow.ocp_mtv_operator import plan_create
from lib.workflow.ocp_mtv_operator import migration_run

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("mtv")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
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
def set_ocp_mtv_command(ctx, cluster_name, mode, channel, filename, provider, vc_url, vc_user, vc_pass, vc_ssl, vddk, plan, nmap, smap, source, destination, vms, migration_type, target, no_wait, no_confirm):
    """Set mtv operator in openshift cluster"""

    try:
        if mode in ['operator']:
            params = {}
            params['cluster'] = cluster_name
            params['channel'] = channel
            params['confirmation'] = not no_confirm

            success = operator_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['instance']:
            params = {}
            params['cluster'] = cluster_name
            params['instance'] = filename
            params['confirmation'] = not no_confirm

            success = instance_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['provider']:
            params = {}
            params['cluster'] = cluster_name
            params['provider'] = provider
            params['vc-url'] = vc_url
            params['vc-user'] = vc_user
            params['vc-pass'] = vc_pass
            params['vc-ssl'] = vc_ssl
            params['vddk'] = vddk
            params['confirmation'] = not no_confirm

            success = provider_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['nmap']:
            if len(source) == 0:
                ctx.my_output.error('Source network required')
                raise ErrorExit
            
            if len(destination) == 0:
                ctx.my_output.error('Destination network required')
                raise ErrorExit

            if len(source) != len(destination):
                ctx.my_output.error('Source and destination network count must be the same')
                raise ErrorExit

            params = {}
            params['cluster'] = cluster_name
            params['map'] = nmap
            params['source'] = provider
            params['destination'] = 'host'
            params['network'] = []
            for index in range(0, len(source)):
                network = {}
                network['source'] = source[index]
                network['destination'] = destination[index]
                params['network'].append(network)

            params['confirmation'] = not no_confirm

            success = network_map_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
                                    
        if mode in ['smap']:
            if len(source) == 0:
                ctx.my_output.error('Source storage required')
                raise ErrorExit
            
            if len(destination) == 0:
                ctx.my_output.error('Destination storage required')
                raise ErrorExit

            if len(source) != len(destination):
                ctx.my_output.error('Source and destination storage count must be the same')
                raise ErrorExit

            params = {}
            params['cluster'] = cluster_name
            params['map'] = smap
            params['source'] = provider
            params['destination'] = 'host'
            params['storage'] = []
            for index in range(0, len(source)):
                storage = {}
                storage['source'] = source[index]
                storage['destination'] = destination[index]
                params['storage'].append(storage)

            params['confirmation'] = not no_confirm

            success = storage_map_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['plan']:
            params = {}
            params['cluster'] = cluster_name
            params['plan'] = plan
            params['source'] = provider
            params['destination'] = 'host'
            params['network'] = nmap
            params['storage'] = smap
            params['vm'] = []
            for item in vms:
                params['vm'].append(item)
            params['type'] = migration_type
            params['target'] = target
            params['confirmation'] = not no_confirm

            success = plan_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['run']:
            params = {}
            params['cluster'] = cluster_name
            params['action'] = 'run'
            params['plan'] = plan
            params['wait'] = not no_wait
            params['confirmation'] = not no_confirm

            success = migration_run.run(
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
