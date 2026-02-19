import sys
import traceback
import click

from lib.workflow.ocp_bashrc_proxy import configure as bashrc

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("bashrc")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--http_proxy", default='', callback=validations.empty_string_to_none, help="http proxy")
@click.option("--https_proxy", default='', callback=validations.empty_string_to_none, help="https proxy")
@click.option("--no_proxy", default='', callback=validations.empty_string_to_none, help="no proxy")
@click.option("--inherit", is_flag=True, show_default=True, default=False, help="Inherit from cluster proxy")
def set_ocp_bashrc_command(
        ctx,
        cluster_name,
        http_proxy,
        https_proxy,
        no_proxy,
        inherit
        ):
    """Set ocp cluster bashrc proxy settings"""

    # iserver set ocp bashrc

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['http_proxy'] = http_proxy
        params['https_proxy'] = https_proxy
        params['no_proxy'] = no_proxy
        params['inherit'] = inherit

        success = bashrc.run(
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
