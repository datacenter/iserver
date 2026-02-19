import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_odf_operator import operator_create
from lib.workflow.ocp_odf_operator import cluster_create

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("odf")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'cluster', 'all'], case_sensitive=False), default='operator', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="ODF Cluster")
@click.option("--sc", "storage_class", default='odf-sc', callback=validations.empty_string_to_none, show_default=True, help="Storage class name")
@click.option("--replica", default=0, type=click.INT, show_default=True, help="Replica")
@click.option("--count", default=0, type=click.INT, show_default=True, help="Count")
@click.option("--default-sc", is_flag=True, show_default=True, default=False, help="Set ODF storage class as default")
@click.option("--nfs", is_flag=True, show_default=True, default=False, help="Enable nfs")
@click.option("--flexible", is_flag=True, show_default=True, default=False, help="Flexible scaling")
@click.option("--tools", is_flag=True, show_default=True, default=False, help="Ceph tools")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_odf_command(
        ctx, 
        cluster_name, 
        mode, 
        channel, 
        filename,
        storage_class,
        replica,
        count,
        default_sc,
        nfs,
        flexible,
        tools,
        no_confirm
    ):
    """Set openshift data foundation operator in openshift cluster"""

    try:
        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['channel'] = channel
            params['confirmation'] = not no_confirm

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
            params['sc'] = storage_class
            params['replica'] = replica
            params['count'] = count
            params['default_sc'] = default_sc
            params['nfs'] = nfs
            params['flexible'] = flexible
            params['tools'] = tools
            params['confirmation'] = not no_confirm

            success = cluster_create.run(
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
