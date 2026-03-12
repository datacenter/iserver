import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_oauth import restart
from lib.workflow.ocp_oauth import debug

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("oauth")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['log', 'restart'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--scope", type=click.Choice(['oauth', 'operator'], case_sensitive=False), default='oauth', show_default=True, help="Restart deployment")
@click.option("--level", type=click.Choice(['Normal', 'Debug', 'Trace', 'TraceAll'], case_sensitive=False), default='Normal', show_default=True, help="Debug level")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_oauth_command(
        ctx,
        cluster_name,
        mode,
        scope,
        level,
        no_confirm
    ):
    """Set authantication in openshift cluster"""

    try:
        if mode in ['log']:
            params = {}
            params['cluster'] = cluster_name
            params['level'] = level
            params['confirmation'] = not no_confirm

            success = debug.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['restart']:
            params = {}
            params['cluster'] = cluster_name
            params['scope'] = scope
            params['confirmation'] = not no_confirm

            success = restart.run(
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
