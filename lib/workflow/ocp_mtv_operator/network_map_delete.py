from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'nmap_namespace' not in params:
        params['nmap_namespace'] = None

    if 'nmap_name' not in params:
        params['nmap_name'] = None

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
        'nmap_namespace',
        'nmap_name',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Network Map', before_newline=True, after_newline=True, double_underline=True)

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
    if params['nmap_namespace'] is not None:
        object_filter.append('namespace:%s' % (params['nmap_namespace']))
    if params['nmap_name'] is not None:
        object_filter.append('name:%s' % (params['nmap_name']))

    maps = params['k8s_handler'].get_network_maps(
        object_filter=object_filter, 
        plan_info=True, 
        cache_enabled=False
    )
    if maps is None:
        my_output.error('Failed to get network maps')
        return False
    
    if len(maps) == 0:
        my_output.default('No network map defined')
        return True
    
    k8s_output_handler.print_network_maps(maps)

    if params['confirmation']:
        if not get_confirmation():
            return False
    
    used = []
    for nmap in maps:
        if len(nmap['plan']) > 0:
            used.append(
                nmap['namespace_name']
            )

    if len(used) > 0:
        my_output.my_list(
            used,
            title='Network maps being used and not to be deleted',
            underline=False,
            before_newline=True,
            ending_newline=True
        )

    for nmap in maps:
        if len(nmap['plan']) > 0:
            continue

        success = params['k8s_handler'].delete_network_map(
            nmap['namespace'], 
            nmap['name'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- selected network maps deleted')
    if len(used) > 0:
        my_output.default('- network maps used by migration plans not deleted')

    return True
