import os
import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_tetragon_operator import operator_create
from lib.workflow.ocp_prometheus import monitoring_enable
from lib.workflow.ocp_tetragon_operator import prometheus_enable
from lib.workflow.ocp_tetragon_operator import crd_create

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("tetragon")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'prometheus', 'crd', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--image", default='', callback=validations.empty_string_to_none, show_default=True, help="Tetragon Enterprise Operator image")
@click.option("--crd", multiple=True, show_default=True, help="Tetragon policy directory or file")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_tetragon_command(
        ctx,
        cluster_name,
        mode,
        channel,
        image,
        crd,
        no_confirm
    ):
    """Set tetragon enterprise operator in openshift cluster"""
    try:
        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['channel'] = channel
            params['image'] = image
            params['confirmation'] = not no_confirm
                
            success = operator_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['prometheus', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm
            
            success = monitoring_enable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm
                
            success = prometheus_enable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['crd', 'all']:
            if mode == 'crd' or len(crd) > 0:
                params = {}
                params['cluster'] = cluster_name
                params['crd'] = crd
                params['confirmation'] = not no_confirm
                    
                success = crd_create.run(
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
