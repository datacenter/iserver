import json
from lib import output_helper
from lib.workflow.ocp_cilium_pnet import common as local_common
from lib.workflow import ocp_common


def validate(params):
    # rules = [
    #     ['cluster', False, None, 'str', None, None, None, None],
    #     ['mode', True, 'default', 'str', None, None, ['default', 'bridge', 'local-access'], None]
    # ]
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['option', True, [], 'list-of-str', None, None, ['multus', 'local-access', 'net-binding', 'webhook', 'certmanager'], None],
        ['option-mode', True, 'add', 'str', None, None, ['add', 'set'], None],        
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Enable')
    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False
    
    state = params['k8s_handler'].get_clusterwide_private_network_state(cache_enabled=False)
    if state['enabled']:
        my_output.default('Private network already enabled')
        my_output.default(json.dumps(state['configuration'], indent=4), wrap='~~~')
    else:
        success = params['k8s_handler'].enable_cilium_private_network(
            my_output=my_output, 
            confirmation=params['confirmation']
        )
        if not success:
            return False        

    if not local_common.is_pnet_crd(params, my_output=my_output):
        return False
    
    # if params['fixup']:
    #     my_output.default('Workaround patch', underline=True, before_newline=True)
    #     my_output.default('Delete crd clusterwideprivatenetworks.isovalent.com')
    #     success = params['k8s_handler'].delete_custom_resource_definition_mo('clusterwideprivatenetworks.isovalent.com')
    #     if not success:
    #         my_output.error('rest api failed')
    #         return False
        
    #     if not params['k8s_handler'].restart_deployment('cilium', 'cilium-operator', my_output=my_output):
    #         return False

    #     if not params['k8s_handler'].wait_cilium_resources(my_output=my_output):
    #         return False
            
    #     if not local_common.is_pnet_crd(params, my_output=my_output):
    #         return False        

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network feature enabled')
    return True