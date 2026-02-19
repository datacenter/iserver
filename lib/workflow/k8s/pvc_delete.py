from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.k8s import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'namespace' not in params:
        params['namespace'] = None

    if 'name' not in params:
        params['name'] = None

    if 'unused' not in params:
        params['unused'] = False

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    allowed_keys = [
        'cluster',
        'namespace',
        'name',
        'unused',
        'verbose',
        'check-verbose',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - PVC - Delete', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    pvcs = local_common.get_pvcs(
        params['k8s_handler'],
        namespace=params['namespace'], 
        name=params['name'], 
        unused=params['unused']
    )
    if pvcs is None:
        my_output.error('Failed to get pvcs')
        return False
    
    if len(pvcs) == 0:
        my_output.default('No pvc found')
        return True
    
    k8s_output_handler.print_pvcs(pvcs)

    if params['confirmation']:
        if not get_confirmation():
            return False

    my_output.default('Delete pvc', before_newline=True)

    success = True
    used = []
    for pvc_info in pvcs:
        if pvc_info['used']:
            my_output.default('- %s/%s (skipping used)' % (pvc_info['namespace'], pvc_info['name']))
            used.append(pvc_info)
            continue

        if pvc_info['dv_name'] is None:
            delete_mo = params['k8s_handler'].delete_pvc_mo(pvc_info['namespace'], pvc_info['name'])
            if delete_mo:
                my_output.default('- pvc %s/%s (%s)' % (pvc_info['namespace'], pvc_info['name'], my_output.add_color('success', 'Green')))
                if not params['k8s_handler'].wait_no_pvc(pvc_info['namespace'], pvc_info['name']):
                    my_output.error('Timed out waiting for no pvc')
                    delete_mo = False
            else:
                my_output.default('- pvc %s/%s (%s)' % (pvc_info['namespace'], pvc_info['name'], my_output.add_color('failed', 'Red')))

            success = success and delete_mo

        if pvc_info['dv_name'] is not None:
            delete_mo = params['k8s_handler'].delete_data_volume_mo(pvc_info['namespace'], pvc_info['dv_name'])
            if delete_mo:
                my_output.default('- dv %s/%s (%s)' % (pvc_info['namespace'], pvc_info['dv_name'], my_output.add_color('success', 'Green')))
                if not params['k8s_handler'].wait_no_pvc(pvc_info['namespace'], pvc_info['name']):
                    my_output.error('Timed out waiting for no pvc')
                    delete_mo = False
            else:
                my_output.default('- dv %s/%s (%s)' % (pvc_info['namespace'], pvc_info['dv_name'], my_output.add_color('failed', 'Red')))

            success = success and delete_mo

    if len(used) > 0:
        my_output.default('Used pvcs not deleted', before_newline=True)

    if not success:
        my_output.error('Some delete api calls failed', before_newline=True)

    return success
