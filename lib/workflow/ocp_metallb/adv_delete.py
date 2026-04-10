from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_metallb import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['advertisement', True, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - MetalLB Operator - Delete bgp advertisement', before_newline=True, after_newline=True, double_underline=True)

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
    
    if params['advertisement'] is None:
        advertisements = params['k8s_handler'].get_bgp_advertisements(cache_enabled=False)
        if advertisements is None:
            my_output.error('failed to get BGPPeer crds')
            return False
        
        k8s_output_handler.print_bgp_advertisements(advertisements)
        if len(advertisements) == 0:
            return True
        
        advertisement_index = my_output.get_integer(prompt='Select advertisement by index (0=all)', min_value=0, max_value=len(advertisements))
        if advertisement_index == 0:
            params['advertisement'] = '__all__'
        else:
            params['advertisement'] = advertisements[advertisement_index-1]['name']

    if params['advertisement'] == '__all__':
        advertisements = params['k8s_handler'].get_bgp_advertisements(cache_enabled=False)
        if advertisements is None:
            my_output.error('failed to get BGPPeer crds')
            return False
        
        k8s_output_handler.print_bgp_advertisements(advertisements)
        if len(advertisements) == 0:
            my_output.default('No bgp advertisement found')
            return True
        
        for advertisement in advertisements:
            success = params['k8s_handler'].delete_bgp_advertisement(
                advertisement['namespace'], 
                advertisement['name'], 
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False
            
    if params['advertisement'] != '__all__':
        success = params['k8s_handler'].delete_bgp_advertisement(
            params['__default__']['namespace'], 
            params['advertisement'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False

    advertisements = params['k8s_handler'].get_bgp_advertisements(cache_enabled=False)
    if advertisements is None:
        my_output.error('failed to get BGPPeer crds')
        return False
    
    k8s_output_handler.print_bgp_advertisements(advertisements)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- MetalLB bgp advertisement deleted')

    return True
