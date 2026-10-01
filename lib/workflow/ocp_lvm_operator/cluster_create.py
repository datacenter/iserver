from lib.k8s import output as k8s_output
from lib import output_helper
from lib import file_helper
from lib.linux import output as linux_output
from lib.workflow.ocp_lvm_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['filename', True, None, 'file-k8s', None, None, None, None],
        ['chunk', True, None, 'str', None, None, None, None],
        ['device', True, [], 'list-of-str', None, None, None, None],
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ssh_required = False
    if len(params['device']) > 0:
        ssh_required = True

    ocp_common.print_title(params, my_output, 'Create Instance')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=ssh_required)
    if params is None:
        return False

    if not local_common.is_lvm_ready(params, my_output, check_lvm_cluster=True, instance_allowed=False, instance_required=False):
        return False
                
    instance_body = None
    if params['filename'] is not None:
        instance_body = file_helper.get_file_yaml(
            params['filename']
        )
        if instance_body is None:
            my_output.error('Failed to get cluster definition: %s' % (params['filename']))
            return False
                
    devices = None
    if len(params['device']) == 0:
        my_output.default('Devices not defined')

    if len(params['device']) > 0:
        devices = local_common.get_devices_path(
            params['cluster'],
            params['k8s_handler'],
            params['device'],
            linux_output_handler,
            my_output,
            log_id=log_id
        )
        if devices is None:
            return False

    success = params['k8s_handler'].create_lvm_cluster(
        devices=devices, 
        chunk_size=params['chunk'],
        body=instance_body, 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    lvmc = params['k8s_handler'].get_lvm_cluster(cache_enabled=False)
    k8s_output_handler.print_lvm_cluster(lvmc)

    storage_class = params['k8s_handler'].get_storage_class_lvm(cache_enabled=False)
    k8s_output_handler.print_storage_classes([storage_class])

    if ssh_required:
        linux_lvm_info = local_common.get_linux_lvm(
            params['cluster'],
            params['k8s_handler'],
            my_output,
            log_id=log_id
        )

        local_common.print_linux_lvm(
            linux_lvm_info,
            linux_output_handler
        )

    if lvmc['ready']:
        my_output.default('')
        my_output.default('Completed tasks')
        my_output.default('- LVM Cluster instance created and ready')
        my_output.default('- Storage class ready')

    if not lvmc['ready']:
        my_output.default('')
        my_output.default('Completed tasks')
        my_output.default('- LVM Cluster instance created')
        my_output.default('- Storage class ready')
        my_output.default('- Cluster instance state: %s' % (my_output.add_color(lvmc['state'], 'Red')))

    return True