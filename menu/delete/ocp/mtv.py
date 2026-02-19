import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_mtv_operator import operator_delete
from lib.workflow.ocp_mtv_operator import instance_delete
from lib.workflow.ocp_mtv_operator import plan_delete
from lib.workflow.ocp_mtv_operator import network_map_delete
from lib.workflow.ocp_mtv_operator import storage_map_delete
from lib.workflow.ocp_mtv_operator import provider_delete

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("mtv")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'provider', 'smap', 'nmap', 'plan', 'wipe', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--wipe", is_flag=True, default=False, show_default=True, help="Wipe plans")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_mtv_command(ctx, cluster_name, mode, namespace, name, wipe, no_confirm):
    """Delete mtv operator in openshift cluster"""

    try:
        if mode in ['plan', 'wipe', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['plan_namespace'] = namespace
            params['plan_name'] = name
            params['wipe'] = wipe
            params['confirmation'] = not no_confirm

            success = plan_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['nmap', 'wipe', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['nmap_namespace'] = namespace
            params['nmap_name'] = name
            params['confirmation'] = not no_confirm

            success = network_map_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
                    
        if mode in ['smap', 'wipe', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['smap_namespace'] = namespace
            params['smap_name'] = name
            params['confirmation'] = not no_confirm

            success = storage_map_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['provider', 'wipe', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['provider_name'] = name
            params['confirmation'] = not no_confirm

            success = provider_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
                                
        if mode in ['instance', 'all']:
            params = {}
            params['cluster'] = cluster_name

            success = instance_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name

            success = operator_delete.run(
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
