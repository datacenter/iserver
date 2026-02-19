import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_local_storage_operator import operator_create
from lib.workflow.ocp_local_storage_operator import volume_create

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("lso")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'volume','all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--nso", is_flag=True, show_default=True, default=False, help="Enable node selector override namespace annotation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--sc", "storage_class", default='local-sc', callback=validations.empty_string_to_none, show_default=True, help="Storage class name")
@click.option("--device", is_flag=False, multiple=True, help="Device for local volumes")
@click.option("--limit", "device_limit", is_flag=False, multiple=True, help="Device discovery limitations")
@click.option("--volume", type=click.Choice(['block', 'fs'], case_sensitive=False), default='block', show_default=True, help="Volume mode")
@click.option("--fs", "fstype", default='ext4', callback=validations.empty_string_to_none, show_default=True, help="Filesystem type if filesystem volume")
@click.option("--max", "max_count", default=-1, type=click.INT, show_default=True, help="Max discovered devices per node (default unlimited)")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_lso_command(
        ctx, 
        cluster_name, 
        nso, 
        channel, 
        mode,
        storage_class,
        device,
        device_limit,
        volume,
        fstype,
        max_count,
        no_confirm 
    ):
    """Set local storage operator in openshift cluster"""

    try:
        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['node-selector-override'] = nso
            params['channel'] = channel
            params['confirmation'] = not no_confirm

            success = operator_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['volume', 'all']:
            new_device = []
            for item in device:
                new_device.append(item)

            new_limit = []
            for item in device_limit:
                new_limit.append(item)

            params = {}
            params['cluster'] = cluster_name
            params['sc'] = storage_class
            params['device'] = new_device
            params['limit'] = new_limit
            params['volume'] = volume
            params['fstype'] = fstype
            params['max'] = max_count
            params['confirmation'] = not no_confirm

            success = volume_create.run(
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
