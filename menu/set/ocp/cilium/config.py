import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_cni import configure as ocp_workflow


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("config")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--filename", default='', callback=validations.empty_string_to_none, show_default=True, help="Target configuration")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
@click.option("--no-rollback", "no_rollback", is_flag=True, show_default=True, default=False, help="Rollback mode")
def set_ocp_cilium_config_command(ctx, cluster_name, filename, no_wait, no_confirm, no_rollback):
    """Set cilium configuration"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['filename'] = filename
        params['wait'] = not no_wait
        params['confirmation'] = not no_confirm
        params['rollback'] = not no_rollback

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
