from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_lvm_operator import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'

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
        'ssh-required',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def delete_unused(params, resources, my_output):
    if len(resources['pvc']) == 0 and len(resources['snapshot']) == 0:
        my_output.default('No resources to be deleted', before_newline=True)
        return True
    
    to_delete = False
    for pvc in resources['pvc']:
        if not pvc['used']:
            to_delete = True
            for snapshot in resources['snapshot']:
                if snapshot['namespace'] == pvc['namespace'] and snapshot['info']['pvc'] == pvc['name']:
                    my_output.default('- snapshot [%s] will be deleted' % (snapshot['namespace_name']))

            my_output.default('- pvc [%s] will be deleted' % (pvc['namespace_name']))

    if not to_delete:
        my_output.default('No usused resources to be deleted', before_newline=True)
        return True        
    
    if params['confirmation']:
        if not get_confirmation(before_newline=True):
            return False

    for pvc in resources['pvc']:
        if not pvc['used']:
            for snapshot in resources['snapshot']:
                if snapshot['namespace'] == pvc['namespace'] and snapshot['info']['pvc'] == pvc['name']:
                    success = params['k8s_handler'].delete_volume_snapshot(snapshot['namespace'], snapshot['name'])
                    if not success:
                        my_output.error('Volume snapshot delete failed: %s' % (snapshot['namespace_name']))
                        return False
                    
                    my_output.default('- volume snapshot deleted: [%s]' % (snapshot['namespace_name']))
                    my_output.default('- wait for no snapshot...')
                    if not params['k8s_handler'].wait_no_volume_snapshot(snapshot['namespace'], snapshot['name']):
                        my_output.error('Volume snapshot still there')
                        return False

            success = params['k8s_handler'].delete_pvc_mo(pvc['namespace'], pvc['name'])
            if not success:
                my_output.error('PVC delete failed: [%s]' % (pvc['namespace_name']))
                return False

            my_output.default('PVC deleted: [%s]' % (pvc['namespace_name']))
            my_output.default('- wait for no pvc...')
            if not params['k8s_handler'].wait_no_pvc(pvc['namespace'], pvc['name']):
                my_output.error('PVC still there')
                return False
            
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - LVM Operator - Delete Unused PVC and Volume Snapshots', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_lvm_ready(params, my_output, check_lvm_cluster=True, instance_required=True, ready_required=False):
        return False
    
    resources = local_common.get_lvm_resources(
        params,
        my_output,
        title='Current Resources',
        pvc=True,
        snapshot=True,
        k8s_output_handler=k8s_output_handler
    )
    if resources is None:
        return False
    
    if not delete_unused(params, resources, my_output):
        return False
    
    resources = local_common.get_lvm_resources(
        params,
        my_output,
        title='Resources After Delete',
        pvc=True,
        snapshot=True,
        k8s_output_handler=k8s_output_handler
    )

    return True
