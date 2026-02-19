import os
import sys
import traceback
import click

from lib.workflow.ocp_cilium_cli import install as cilium

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cli-cilium")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--url", default='', callback=validations.empty_string_to_none, help="Cilium download url")
@click.option("--version", default='', callback=validations.empty_string_to_none, help="Cilium version")
def set_ocp_cli_cilium(
        ctx,
        cluster_name,
        url,
        version
        ):
    """Set ocp cluster cilium cli"""

    # iserver set ocp cilium

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['url'] = url
        params['version'] = version

        success = cilium.run(
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
