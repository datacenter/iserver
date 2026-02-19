import os
import json
import yaml
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_odf_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'sc' not in params:
        params['sc'] = 'odf-sc'

    if not isinstance(params['sc'], str):
        return None, 'sc param must be string'

    if 'replica' not in params:
        return None, 'Replica required'

    if not isinstance(params['replica'], int):
        return None, 'replica param must be int'
    
    if params['replica'] <= 0:
        return None, 'replica param must be gt 0'

    if 'count' not in params:
        return None, 'Count required'

    if not isinstance(params['count'], int):
        return None, 'count param must be int'
    
    if params['count'] <= 0:
        return None, 'count param must be gt 0'

    if 'default_sc' not in params:
        params['default_sc'] = False

    if not isinstance(params['default_sc'], bool):
        return None, 'default_sc param must be true or false'
    
    if 'nfs' not in params:
        params['nfs'] = False

    if not isinstance(params['nfs'], bool):
        return None, 'nfs param must be true or false'

    if 'flexible' not in params:
        params['flexible'] = False

    if not isinstance(params['flexible'], bool):
        return None, 'flexible param must be true or false'
    
    if 'tools' not in params:
        params['tools'] = False

    if not isinstance(params['tools'], bool):
        return None, 'tools param must be true or false'
    
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
        
    if 'confirmation' not in params:
        params['confirmation'] = False

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'instance',
        'sc',
        'replica',
        'count',
        'default_sc',
        'nfs',
        'flexible',
        'tools',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Create Cluster', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    my_output.default('Checks', before_newline=True, underline=True)
    if not params['k8s_handler'].is_odf_subscription(params['namespace'], params['name']):
        my_output.error('ODF must be created first')
        return False
    my_output.default('- odf subscription found')

    if params['k8s_handler'].is_storage_cluster(cache_enabled=False):
        my_output.default('ODF cluster already defined')
        return True
    
    if params['instance'] is None:
        lso_sc = params['k8s_handler'].get_storage_class_name_local_storage()
        if lso_sc is None:
            my_output.error('Local storage class not found')
            return False
        my_output.default('- local storage class: %s' % (lso_sc))
        
        pv = params['k8s_handler'].get_pvs(
            object_filter=['sc:%s' % (lso_sc)],
            cache_enabled=False
        )
        if pv is None:
            my_output.error('Failed to get pv for local storage')
            return False
        my_output.default('- persistent volumes for local storage: %s' % (len(pv)))

        if params['replica'] * params ['count'] > len(pv):
            my_output.error('Not enough pv for replica/count')
            return False
        my_output.default('- enough pvs for repliaca [%s] and count [%s]' % (params['replica'], params['count']))
    
    if params['instance'] is None:
        success = params['k8s_handler'].create_storage_cluster_from_params(
            params['namespace'],
            params['cluster-name'],
            params['sc'],
            lso_sc,
            params['count'],
            params['replica'],
            default_sc=params['default_sc'],
            default_virt_sc=params['default_sc'],
            flexible_scaling=params['flexible'],
            nfs=params['nfs'],
            tools=params['tools'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    if params['instance'] is not None:
        success = params['k8s_handler'].create_storage_cluster_from_body(
            params['namespace'],
            params['cluster-name'],
            params['instance'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cluster created and ready')

    return True
