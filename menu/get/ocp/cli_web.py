import sys
import traceback
import click

from lib.workflow.ocp_web_terminal_operator import get as web

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cli-web")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
def get_ocp_cli_web(
        ctx,
        cluster_name
        ):
    """Get ocp cluster cli web terminal"""

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name

        success = web.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
