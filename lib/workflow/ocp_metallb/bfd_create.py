from lib import filter_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_metallb import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def get_bfd_body(params, my_output):
    body = {}
    body['apiVersion'] = 'metallb.io/v1beta1'
    body['kind'] = 'BFDProfile'
    body['metadata'] = {}
    body['metadata']['namespace'] = params['__default__']['namespace']
    body['metadata']['name'] = my_output.get_value('BFD profile crd name', empty=True)
    if body['metadata']['name'] is None or len(body['metadata']['name']) == 0:
        return None
    
    current_bfd = params['k8s_handler'].get_bfd_profile(body['metadata']['namespace'], body['metadata']['name'], return_mo=True, cache_enabled=True)
    if current_bfd is not None:
        body['metadata']['resourceVersion'] = current_bfd['metadata']['resourceVersion']
        my_output.default('BFD profile name already defined and will be updated')
    
    body['spec'] = {}
    body['spec']['detectMultiplier'] = my_output.get_integer(
        'detectMultiplier', 
        default=filter_helper.get(
            current_bfd, 
            'spec:detectMultiplier', 
            on_error=3, 
            on_none=3
        )
    )
    body['spec']['echoMode'] = my_output.get_bool(
        'echoMode', 
        default=filter_helper.get(
            current_bfd, 
            'spec:echoMode', 
            on_error=False, 
            on_none=False
        )
    )
    body['spec']['echoInterval'] = my_output.get_integer(
        'echoInterval', 
        default=filter_helper.get(
            current_bfd, 
            'spec:echoInterval', 
            on_error=50, 
            on_none=50
        )
    )
    body['spec']['minimumTtl'] = my_output.get_integer(
        'minimumTtl', 
        default=filter_helper.get(
            current_bfd, 
            'spec:minimumTtl', 
            on_error=254, 
            on_none=254
        )
    )
    body['spec']['passiveMode'] = my_output.get_bool(
        'passiveMode', 
        default=filter_helper.get(
            current_bfd, 
            'spec:passiveMode', 
            on_error=False, 
            on_none=False
        )
    )
    body['spec']['receiveInterval'] = my_output.get_integer(
        'receiveInterval', 
        default=filter_helper.get(
            current_bfd, 
            'spec:receiveInterval', 
            on_error=300, 
            on_none=300
        )
    )
    body['spec']['transmitInterval'] = my_output.get_integer(
        'transmitInterval', 
        default=filter_helper.get(
            current_bfd, 
            'spec:transmitInterval', 
            on_error=300, 
            on_none=300
        )
    )
    return body


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - MetalLB Operator - Create bfd profile', before_newline=True, after_newline=True, double_underline=True)

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

    bfds = params['k8s_handler'].get_bfd_profiles(cache_enabled=False)
    if bfds is None:
        my_output.error('failed to get BFDProfile crds')
        return False
    
    k8s_output_handler.print_bfd_profiles(bfds)
    my_output.default('')

    body = get_bfd_body(params, my_output)
    if body is None:
        return False
    
    success = params['k8s_handler'].create_or_update_bfd_profile(
        body, 
        my_output=my_output, 
        confirmation=params['confirmation'], 
        wait=params['wait']
    )
    if not success:
        return False
    
    bfds = params['k8s_handler'].get_bfd_profiles(cache_enabled=False)
    if bfds is None:
        my_output.error('failed to get BFDProfile crds')
        return False
    
    k8s_output_handler.print_bfd_profiles(bfds)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- MetalLB bfd profile defined')

    return True
