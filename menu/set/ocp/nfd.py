import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_nfd_operator import operator_create as ocp_installer

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("nfd")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator'], case_sensitive=False), default='operator', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="NodeFeatureDiscovery CRD")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_nfd_command(ctx, cluster_name, channel, filename, mode, no_confirm):
    """Set nfd operator in openshift cluster"""

    try:
        if mode == 'operator':
            params = {}
            params['cluster'] = cluster_name
            params['channel'] = channel
            params['instance'] = filename
            params['confirmation'] = not no_confirm

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
