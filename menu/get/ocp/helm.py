import sys
import traceback
import threading
import click

from lib.ocp import output as ocp_output
from lib.workflow.ocp_access import check as ocp_check

from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("helm")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.validate_ocp_cluster_name_no_prompt, help="Filter by cluster name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_helm_command(
        ctx,
        cluster_name,
        output,
        devel
        ):
    """Get ocp helm state"""

    # iserver get ocp helm

    ctx.developer = devel
    ctx.output = output

    try:
        ocp_output_handler = ocp_output.OcpOutput(log_id=ctx.run_id)

        ocp_check_params = {}
        ocp_check_params['cluster'] = cluster_name
        ocp_check_params['cli-helm-required'] = True
        ocp_check_params['verbose'] = True
        ocp_params, errors = ocp_check.run(
            ocp_check_params,
            log_id=ctx.run_id
        )
        if errors is not None:
            ctx.my_output.error(errors)
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        charts = ocp_params['data']['ocp_handler'].get_ocp_helm_mo()
        ctx.busy = False
        ocp_output_handler.print_ocp_helm(charts, title=False)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
