import os
import sys
import traceback
import click

from lib.workflow.ocp_helm_cli import get as helm

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cli-helm")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--view", "-v", default=['list'], help="[list|ver|all]", show_default=True, multiple=True)
def get_ocp_cli_helm(
        ctx,
        cluster_name,
        view
        ):
    """Get ocp cluster helm"""

    ctx.developer = False
    ctx.output = 'default'
    view = validations.validate_view(
        ctx,
        view,
        'list|ver|all',
        'list',
        []
    )
    if view is None:
        sys.exit(1)
        
    try:
        params = {}
        params['cluster'] = cluster_name
        params['view'] = view

        success = helm.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

        ctx.my_output.default('View: list (def), ver, all', before_newline=True)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
