import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_nfd_operator import get as ocp_installer

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("nfd")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Show node annotations")
def get_ocp_nfd_command(ctx, cluster_name, verbose):
    """Get nfd operator in openshift cluster"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['annotation'] = verbose

        success = ocp_installer.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

        if not verbose:
            ctx.my_output.default(
                '%s use --verbose to get nfd annotations per node' % (ctx.my_output.add_color('[Note]', 'Blue')),
                before_newline=True
            )

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
