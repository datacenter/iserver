import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_metallb import operator_create
from lib.workflow.ocp_metallb import instance_create
from lib.workflow.ocp_metallb import pool_create
from lib.workflow.ocp_metallb import peer_create
from lib.workflow.ocp_metallb import community_create
from lib.workflow.ocp_metallb import adv_create
from lib.workflow.ocp_metallb import bfd_create


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("metallb")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'all', 'pool', 'peer', 'community', 'adv', 'bfd'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="MetalLB CRD")
@click.option("--bgp", type=click.Choice(['', 'native', 'frr', 'frr-k8s'], case_sensitive=False), default='native', show_default=True, help="BGP backend")
@click.option("--pool", default='', callback=validations.empty_string_to_none, show_default=True, help="IP address pool name")
@click.option("--addr", multiple=True, help="Address pool")
@click.option("--community", multiple=True, help="Community")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_metallb_command(ctx, cluster_name, mode, channel, filename, bgp, pool, addr, community, no_confirm):
    """Set metallb operator in openshift cluster"""

    try:
        if mode in ['operator', 'all']:
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

        if mode in ['instance', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['filename'] = filename
            params['bgp'] = bgp
            params['confirmation'] = not no_confirm

            success = instance_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
        if mode in ['pool']:
            params = {}
            params['cluster'] = cluster_name
            params['pool'] = pool
            params['addr'] = []
            for item in addr:
                params['addr'].append(item)
            params['confirmation'] = not no_confirm

            success = pool_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['peer']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm

            success = peer_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['community']:
            params = {}
            params['cluster'] = cluster_name
            params['community'] = []
            for item in community:
                params['community'].append(item)
            params['confirmation'] = not no_confirm

            success = community_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
                                    
        if mode in ['adv']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm

            success = adv_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
                                    
        if mode in ['bfd']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm

            success = bfd_create.run(
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
