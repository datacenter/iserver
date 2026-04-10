from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_metallb import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['pool', True, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - MetalLB Operator - Delete ip address pool', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output,
        brief=True
    )
    if subscription is None:
        return True
    
    if params['pool'] is None:
        pools = params['k8s_handler'].get_ip_address_pools(cache_enabled=False)
        if pools is None:
            my_output.error('failed to get IPAddressPool crds')
            return False
        
        k8s_output_handler.print_ip_address_pools(pools)
        if len(pools) == 0:
            return True
        
        pool_index = my_output.get_integer(prompt='Select pool by index (0=all)', min_value=0, max_value=len(pools))
        if pool_index == 0:
            params['pool'] = '__all__'
        else:
            params['pool'] = pools[pool_index-1]['name']

    if params['pool'] == '__all__':
        pools = params['k8s_handler'].get_ip_address_pools(cache_enabled=False)
        if pools is None:
            my_output.error('failed to get IPAddressPool crds')
            return False
        
        k8s_output_handler.print_ip_address_pools(pools)
        if len(pools) == 0:
            my_output.default('No ip address pool found')
            return True
        
        for pool in pools:
            success = params['k8s_handler'].delete_ip_address_pool(
                pool['namespace'], 
                pool['name'], 
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False
            
    if params['pool'] != '__all__':
        success = params['k8s_handler'].delete_ip_address_pool(
            params['__default__']['namespace'], 
            params['pool'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False

    pools = params['k8s_handler'].get_ip_address_pools(cache_enabled=False)
    if pools is None:
        my_output.error('failed to get IPAddressPool crds')
        return False
    
    k8s_output_handler.print_ip_address_pools(pools)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- MetalLB ip address pool deleted')

    return True
