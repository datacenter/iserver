from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'smap_namespace' not in params:
        params['smap_namespace'] = None

    if 'smap_name' not in params:
        params['smap_name'] = None

    if 'confirmation' not in params:
        params['confirmation'] = True

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
        'type',
        'smap_namespace',
        'smap_name',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Storage Map', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True

    object_filter = []
    if params['smap_namespace'] is not None:
        object_filter.append('namespace:%s' % (params['smap_namespace']))
    if params['smap_name'] is not None:
        object_filter.append('name:%s' % (params['smap_name']))

    maps = params['k8s_handler'].get_storage_maps(
        object_filter=object_filter, 
        plan_info=True, 
        cache_enabled=False
    )
    if maps is None:
        my_output.error('Failed to get storage maps')
        return False
    
    if len(maps) == 0:
        my_output.default('No storage map defined')
        return True
    
    k8s_output_handler.print_storage_maps(maps)

    if params['confirmation']:
        if not get_confirmation():
            return False
    
    used = []
    for smap in maps:
        if len(smap['plan']) > 0:
            used.append(
                smap['namespace_name']
            )

    if len(used) > 0:
        my_output.my_list(
            used,
            title='Storage maps being used and not to be deleted',
            underline=False,
            before_newline=True,
            ending_newline=True
        )

    for smap in maps:
        if len(smap['plan']) > 0:
            continue

        success = params['k8s_handler'].delete_storage_map(
            smap['namespace'], 
            smap['name'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- selected storage maps deleted')
    if len(used) > 0:
        my_output.default('- storage maps used by migration plans not deleted')

    return True
