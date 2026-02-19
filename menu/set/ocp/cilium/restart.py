import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_cni import restart as ocp_workflow

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("restart")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'agent', 'all'], case_sensitive=False), default='all', show_default=True, help="Mode of operation")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
def set_ocp_cilium_restart_command(ctx, cluster_name, mode, no_wait):
    """Restart cilium components"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['operator'] = mode in ['operator', 'all']
        params['agent'] = mode in ['agent', 'all']
        params['wait'] = not no_wait

        success = ocp_workflow.run(
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
