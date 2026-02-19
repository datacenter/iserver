import sys
import traceback
import click
from lib.workflow.ocp_lvm_operator import test
from lib.workflow.ocp_lvm_operator import cluster_create
from lib.workflow.ocp_lvm_operator import operator_create

from menu import validations

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("lvm")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'cluster', 'all', 'test'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="LVM Cluster")
@click.option("--device", is_flag=False, multiple=True, help="Device names for lvm storage")
@click.option("--chunk", default='', callback=validations.empty_string_to_none, help="Chunk size")
@click.option("--test-namespace", "test_namespace", default='test-lvm', show_default=True, help="Test namespace")
@click.option("--keep", is_flag=True, show_default=True, default=False, help="Keep test resources")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_lvm_command(
        ctx, 
        cluster_name, 
        channel,
        mode,
        filename,
        device,
        chunk,
        test_namespace, 
        keep,
        verbose,
        no_confirm
    ):
    """Set logical volume manager storage operator in openshift cluster"""

    try:
        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['channel'] = channel
            params['confirmation'] = not no_confirm
            params['verbose'] = verbose
            
            success = operator_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['cluster', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['filename'] = filename
            params['device'] = device
            params['chunk'] = chunk
            params['confirmation'] = not no_confirm
            params['verbose'] = verbose
            
            success = cluster_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'test':
            params = {}
            params['cluster'] = cluster_name
            params['test-namespace'] = test_namespace
            params['ssh-required'] = True
            params['cleanup'] = not keep
            params['confirmation'] = not no_confirm
            params['verbose'] = verbose

            success = test.run(
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
