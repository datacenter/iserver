import os
from lib.k8s import output as k8s_output
from lib import output_helper
from lib import file_helper
from lib.linux import output as linux_output
from lib.workflow.ocp_lvm_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'ssh-check' not in params:
        params['ssh-check'] = True

    if not isinstance(params['ssh-check'], bool):
        return None, 'ssh-check param must be true or false'

    params['instance'] = None
    if 'filename' in params and params['filename'] is not None:
        try:
            print(params['filename'])
            if not os.path.isabs(params['filename']):
                params['filename'] = os.path.join(
                    params['base_directory'],
                    params['filename']
                )
        except BaseException:
            return None, 'LVM cluster file path detection failed'
        
        params['instance'] = file_helper.get_file_yaml(
            params['filename']
        )
        if params['instance'] is None:
            return None, 'Yaml file read failed: %s' % (params['filename'])
        
        if 'kind' not in params['instance']:
            return None, 'Invalid yaml file content: %s' % (params['filename'])

    if 'chunk' not in params:
        params['chunk'] = None
            
    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'

    if 'device' not in params:
        params['device'] = []

    params['ssh-required'] = False
    if len(params['device']) > 0:
        params['ssh-required'] = True

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'instance',
        'device',
        'chunk',
        'ssh-check',
        'ssh-required',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - LVM Operator - Create Cluster', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh_check=params['ssh-check'], ssh_required=params['ssh-required'])
    if params is None:
        return False

    if not local_common.is_lvm_ready(params, my_output, check_lvm_cluster=True, instance_allowed=False, instance_required=False):
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
        body=params['instance'], 
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

    if params['ssh-ready']:
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

    if lvmc['info']['ready']:
        my_output.default('')
        my_output.default('Completed tasks')
        my_output.default('- LVM Cluster instance created and ready')
        my_output.default('- Storage class ready')

    if not lvmc['info']['ready']:
        my_output.default('')
        my_output.default('Completed tasks')
        my_output.default('- LVM Cluster instance created')
        my_output.default('- Storage class ready')
        my_output.default('- Cluster instance state: %s' % (my_output.add_color(lvmc['info']['state'], 'Red')))

    return True
