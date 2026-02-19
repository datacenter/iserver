import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_nfd_operator import operator_delete as ocp_installer

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("nfd")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator'], case_sensitive=False), default='operator', show_default=True, help="Mode of operation")
def delete_ocp_nfd_command(ctx, cluster_name, mode):
    """Delete nfd operator in openshift cluster"""

    try:
        if mode == 'operator':
            params = {}
            params['cluster'] = cluster_name

            success = ocp_installer.run(
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
