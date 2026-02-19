import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_nmstate_operator import operator_create
from lib.workflow.ocp_nmstate_operator import enable_lldp

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("nmstate")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'lldp', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="NMState CRD")
@click.option("--node", default='', callback=validations.empty_string_to_none, show_default=True, help="Node name")
@click.option("--fw", is_flag=True, show_default=True, default=False, help="Disable LLDP on NIC fw level")
@click.option("--keep-nncp", is_flag=True, show_default=True, default=False, help="Keep NNCP")
@click.option("--skip-down", is_flag=True, show_default=True, default=False, help="Skip interfaces down")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_nmstate_command(
        ctx,
        cluster_name,
        mode,
        channel,
        filename,
        node, 
        fw,
        keep_nncp,
        skip_down,
        no_confirm
    ):
    """Set nmstate operator in openshift cluster"""

    try:
        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['channel'] = channel
            params['instance'] = filename
            params['confirmation'] = not no_confirm

            success = operator_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['lldp', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['settings'] = {}
            params['settings']['enable'] = True
            params['settings']['node'] = node
            params['settings']['nic-fw-disable'] = fw
            params['settings']['delete-nncp'] = not keep_nncp
            params['settings']['include-down'] = not skip_down

            success = enable_lldp.run(
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
