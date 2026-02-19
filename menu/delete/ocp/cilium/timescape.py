import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_timescape import feature_disable


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("timescape")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['feature'], case_sensitive=False), default='feature', show_default=True, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cilium_timescape_command(ctx, cluster_name, mode, no_confirm):
    """Delete cilium timescape"""

    try:
        if mode in ['feature']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm

            success = feature_disable.run(
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
