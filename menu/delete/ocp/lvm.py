import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_lvm_operator import orphan
from lib.workflow.ocp_lvm_operator import unused
from lib.workflow.ocp_lvm_operator import cluster_delete
from lib.workflow.ocp_lvm_operator import operator_delete

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("lvm")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'cluster', 'all', 'orphan', 'unused'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--wipe", is_flag=True, default=False, show_default=True, help="Wipe lvm from disks")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_lvm_command(ctx, cluster_name, mode, wipe, verbose, no_confirm):
    """Delete logical volume manager storage operator in openshift cluster"""

    try:
        if mode == 'orphan':
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm
            params['verbose'] = verbose

            success = orphan.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'unused':
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm
            params['verbose'] = verbose

            success = unused.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
        if mode in ['cluster', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['wipe'] = wipe
            params['confirmation'] = not no_confirm
            params['verbose'] = verbose

            success = cluster_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm
            params['verbose'] = verbose

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
