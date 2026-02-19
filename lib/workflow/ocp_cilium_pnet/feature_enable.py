from lib import output_helper
from lib.workflow.ocp_cilium_pnet import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'fixup' not in params:
        params['fixup'] = False

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
        'channel',
        'fixup',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium Private Network - Enable', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
        return False

    if params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.default('Private network already enabled')
    else:
        success = params['k8s_handler'].enable_cilium_private_network(
            my_output=my_output, 
            confirmation=params['confirmation']
        )
        if not success:
            return False        
    
    if not local_common.is_pnet_crd(params, my_output=my_output):
        return False
    
    if params['fixup']:
        my_output.default('Workaround patch', underline=True, before_newline=True)
        my_output.default('Delete crd clusterwideprivatenetworks.isovalent.com')
        success = params['k8s_handler'].delete_custom_resource_definition('clusterwideprivatenetworks.isovalent.com')
        if not success:
            my_output.error('rest api failed')
            return False
        
        if not params['k8s_handler'].restart_deployment('cilium', 'cilium-operator', my_output=my_output):
            return False

        if not params['k8s_handler'].wait_cilium_resources(my_output=my_output):
            return False
            
        if not local_common.is_pnet_crd(params, my_output=my_output):
            return False        

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network feature enabled')
    my_output.default('- CRD ready')

    return True
