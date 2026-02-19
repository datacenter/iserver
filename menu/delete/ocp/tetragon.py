import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_tetragon_operator import crd_delete
from lib.workflow.ocp_tetragon_operator import operator_delete
from lib.workflow.ocp_tetragon_operator import wipe
from lib.workflow.ocp_tetragon_operator import prometheus_disable


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("tetragon")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'wipe', 'crd', 'prometheus', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--crd", multiple=True, show_default=True, help="Tetragon policy directory or file")
def delete_ocp_tetragon_command(ctx, cluster_name, mode, crd):
    """Delete tetragon operator in openshift cluster"""

    try:
        if mode == 'crd':
            params = {}
            params['cluster'] = cluster_name
            params['crd'] = crd
                
            success = crd_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'prometheus':
            params = {}
            params['cluster'] = cluster_name
                
            success = prometheus_disable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
                            
        if mode in ['wipe', 'all']:
            params = {}
            params['cluster'] = cluster_name

            success = wipe.run(
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
