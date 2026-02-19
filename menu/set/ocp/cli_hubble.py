import os
import sys
import traceback
import click

from lib.workflow.ocp_hubble_cli import install as hubble

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cli-hubble")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--url", default='', callback=validations.empty_string_to_none, help="Hubble download url")
@click.option("--version", default='', callback=validations.empty_string_to_none, help="Hubble version")
def set_ocp_cli_hubble(
        ctx,
        cluster_name,
        url,
        version
        ):
    """Set ocp cluster hubble"""

    # iserver set ocp hubble

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['url'] = url
        params['version'] = version

        success = hubble.run(
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
