import sys
import traceback
import click

from lib.workflow.ocp_web_terminal_operator import operator_create as web

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cli-web")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cli_web(
        ctx,
        cluster_name,
        no_confirm
        ):
    """Set ocp cluster web terminal"""

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['confirmation'] = not no_confirm

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
