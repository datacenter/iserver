import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cnv_operator import operator_delete
from lib.workflow.ocp_cnv_operator import instance_delete
from lib.workflow.ocp_cnv_operator import import_disable

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cnv")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'import', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--wipe", is_flag=True, default=False, show_default=True, help="Wipe dv/pvc")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cnv_command(ctx, cluster_name, mode, wipe, no_confirm):
    """Delete cnv operator in openshift cluster"""

    try:
        if mode in ['import']:
            params = {}
            params['cluster'] = cluster_name
            params['wipe'] = wipe
            params['confirmation'] = not no_confirm

            success = import_disable.run(
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
