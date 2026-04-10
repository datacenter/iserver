from lib import ip_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_metallb import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['pool', True, None, 'str', None, None, None, None],
        ['addr', True, None, 'list-of-ip-range', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - MetalLB Operator - Create ip address pool', before_newline=True, after_newline=True, double_underline=True)

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
    
    pools = params['k8s_handler'].get_ip_address_pools(cache_enabled=False)
    if pools is None:
        my_output.error('failed to get IPAddressPool crds')
        return False

    if params['pool'] is None:
        params['pool'] = 'pool-%s' % (ip_helper.get_short_uuid())
        if params['k8s_handler'].is_ip_address_pool(params['__default__']['namespace'], params['pool']):
            my_output.error('exception on pool name conflict')
            return False

    if len(params['addr']) == 0:
        my_output.error('specifiy at least one address pool')
        return False
    
    success = params['k8s_handler'].create_ip_address_pool(
        params['__default__']['namespace'], 
        params['pool'],
        params['addr'],
        confirmation=params['confirmation'],
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
    my_output.default('- MetalLB ip address pool created')

    return True
