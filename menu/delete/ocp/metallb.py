import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_metallb import operator_delete 
from lib.workflow.ocp_metallb import instance_delete 
from lib.workflow.ocp_metallb import pool_delete
from lib.workflow.ocp_metallb import peer_delete
from lib.workflow.ocp_metallb import community_delete
from lib.workflow.ocp_metallb import adv_delete
from lib.workflow.ocp_metallb import bfd_delete


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("metallb")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'all', 'pool', 'peer', 'community', 'adv', 'bfd', 'wipe', 'nuke'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--pool", default='', callback=validations.empty_string_to_none, show_default=True, help="IP address pool name")
@click.option("--peer", default='', callback=validations.empty_string_to_none, show_default=True, help="BGP peer name")
@click.option("--community", default='', callback=validations.empty_string_to_none, show_default=True, help="Community name")
@click.option("--adv", default='', callback=validations.empty_string_to_none, show_default=True, help="Advertisement name")
@click.option("--bfd", default='', callback=validations.empty_string_to_none, show_default=True, help="BFD profile name")
def delete_ocp_metallb_command(ctx, cluster_name, mode, pool, peer, community, adv, bfd):
    """Delete metallb operator in openshift cluster"""

    try:
        if mode in ['wipe', 'nuke']:
            pool = '__all__'
            peer = '__all__'
            community = '__all__'
            adv = '__all__'
            bfd = '__all__'

        if mode in ['peer', 'wipe', 'nuke']:
            params = {}
            params['cluster'] = cluster_name
            params['peer'] = peer

            success = peer_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['community', 'wipe', 'nuke']:
            params = {}
            params['cluster'] = cluster_name
            params['community'] = community

            success = community_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
        if mode in ['adv', 'wipe', 'nuke']:
            params = {}
            params['cluster'] = cluster_name
            params['advertisement'] = adv

            success = adv_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['bfd', 'wipe', 'nuke']:
            params = {}
            params['cluster'] = cluster_name
            params['bfd'] = bfd

            success = bfd_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
        if mode in ['pool', 'wipe', 'nuke']:
            params = {}
            params['cluster'] = cluster_name
            params['pool'] = pool

            success = pool_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
        if mode in ['instance', 'all', 'nuke']:
            params = {}
            params['cluster'] = cluster_name

            success = instance_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
        if mode in ['operator', 'all', 'nuke']:
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
