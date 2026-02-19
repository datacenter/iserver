import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_iotel import get as ocp_workflow


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("iotel")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--suffix", default='', callback=validations.empty_string_to_none, help="Select suffix by name")
@click.option("--poller", is_flag=True, show_default=True, default=False, help="Show pollers")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def get_ocp_iotel_command(ctx, cluster_name, suffix, poller, verbose, no_confirm):
    """Get openshift intersight open telemetry collector"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['suffix'] = suffix
        params['poller'] = poller
        params['verbose'] = verbose
        params['confirmation'] = not no_confirm

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
