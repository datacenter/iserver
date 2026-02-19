import sys
import traceback
import click

from lib.workflow.ocp_virtctl_cli import install as virtctl

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cli-virtctl")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--url", default='', callback=validations.empty_string_to_none, help="Virtctl package url")
def set_ocp_cli_virtctl(
        ctx,
        cluster_name,
        url
        ):
    """Set ocp cluster virtctl"""

    # iserver set ocp virtctl

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['url'] = url

        success = virtctl.run(
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
