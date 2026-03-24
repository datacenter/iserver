from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.k8s import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['primary', False, False, 'bool', None, None, None, None],
        ['topology', False, False, 'str', None, None, ['l2', 'l3'], None],
        ['subnets', False, [], 'list', None, None, None, None],
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params
        
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('Kubernetes Workflow - OVN User Defined Network - Create', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    if not params['k8s_handler'].is_namespace_udn_enabled(name=params['namespace']):
        my_output.error('Namespace %s is not udn enabled' % (params['namespace']))
        return False
    
    if params['topology'] == 'l2':
        success, error = params['k8s_handler'].validate_user_defined_network_l2_subnets(params['subnets'])
        if not success:
            my_output.error(error)
            return False
        
        if params['primary']:
            udn = params['k8s_handler'].get_namespace_primary_udn(params['namespace'])
            if udn is not None and udn != params['name']:
                my_output.error('Namespace %s already has primary udn %s' % (
                    params['namespace'],
                    params['name']
                ))
                return False
        
        success = params['k8s_handler'].create_user_defined_network_l2(
            params['namespace'],
            params['name'],
            params['primary'],
            subnets=params['subnets'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False

    if params['topology'] == 'l3':
        success, error = params['k8s_handler'].validate_user_defined_network_l3_subnets(params['subnets'])
        if not success:
            my_output.error(error)
            return False
        
        if params['primary']:
            udn = params['k8s_handler'].get_namespace_primary_udn(params['namespace'])
            if udn is not None and udn != params['name']:
                my_output.error('Namespace %s already has primary udn %s' % (
                    params['namespace'],
                    params['name']
                ))
                return False
        
        success = params['k8s_handler'].create_user_defined_network_l3(
            params['namespace'],
            params['name'],
            params['primary'],
            params['subnets'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False

    info = params['k8s_handler'].get_user_defined_network(
        params['namespace'],
        params['name'],
        nad_info=True,
        usage_info=True,
        cache_enabled=False
    )
    k8s_output_handler.print_user_defined_networks_state([info])

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- ovn user defined network created')
    return True
