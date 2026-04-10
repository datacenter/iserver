from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_metallb import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['community', True, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - MetalLB Operator - Delete community', before_newline=True, after_newline=True, double_underline=True)

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
    
    if params['community'] is None:
        communitys = params['k8s_handler'].get_communitys(cache_enabled=False)
        if communitys is None:
            my_output.error('failed to get Community crds')
            return False
        
        k8s_output_handler.print_communitys(communitys)
        if len(communitys) == 0:
            return True
        
        community_index = my_output.get_integer(prompt='Select community by index (0=all)', min_value=0, max_value=len(communitys))
        if community_index == 0:
            params['community'] = '__all__'
        else:
            params['community'] = communitys[community_index-1]['name']

    if params['community'] == '__all__':
        communitys = params['k8s_handler'].get_communitys(cache_enabled=False)
        if communitys is None:
            my_output.error('failed to get Community crds')
            return False
        
        k8s_output_handler.print_communitys(communitys)
        if len(communitys) == 0:
            my_output.default('No community found')
            return True
        
        for community in communitys:
            success = params['k8s_handler'].delete_community(
                community['namespace'], 
                community['name'], 
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False
            
    if params['community'] != '__all__':
        success = params['k8s_handler'].delete_community(
            params['__default__']['namespace'], 
            params['community'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False

    communitys = params['k8s_handler'].get_communitys(cache_enabled=False)
    if communitys is None:
        my_output.error('failed to get Community crds')
        return False
    
    k8s_output_handler.print_communitys(communitys)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- MetalLB community deleted')

    return True
