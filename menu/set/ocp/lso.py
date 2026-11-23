import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("lso")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'volume'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
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
        cluster_names, 
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

    task = {}

    if mode in ['operator']:
        task['operator'] = {}
        task['operator']['channel'] = channel
        task['operator']['node-selector-override'] = nso

    if mode in ['volume']:
        new_device = []
        for item in device:
            new_device.append(item)

        new_limit = []
        for item in device_limit:
            new_limit.append(item)

        task['volume'] = {}
        task['volume']['sc'] = storage_class
        task['volume']['device'] = new_device
        task['volume']['limit'] = new_limit
        task['volume']['volume'] = volume
        task['volume']['fstype'] = fstype
        task['volume']['max'] = max_count

    success = ocp_common.set_workflow(cluster_names, 'lso', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)