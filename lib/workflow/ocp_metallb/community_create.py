from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_metallb import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['community', True, [], 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def get_community_body(params, my_output):
    body = {}
    body['apiVersion'] = 'metallb.io/v1beta1'
    body['kind'] = 'Community'
    body['metadata'] = {}
    body['metadata']['namespace'] = params['__default__']['namespace']
    body['metadata']['name'] = my_output.get_value('Community object name', empty=True)
    if body['metadata']['name'] is None or len(body['metadata']['name']) == 0:
        return None
    
    current_peer = params['k8s_handler'].get_community(body['metadata']['namespace'], body['metadata']['name'], return_mo=True, cache_enabled=True)
    if current_peer is not None:
        body['metadata']['resourceVersion'] = current_peer['metadata']['resourceVersion']
        my_output.default('Community already defined and will be overwritten')
    
    body['spec'] = {}
    body['spec']['communities'] = []

    if len(params['community']) > 0:
        for item in params['community']:
            if len(item.split(':')) != 3:
                my_output.error('community expected format is name:x:y where x:y is community value')
                return None
            
            community = {}
            community['name'] = item.split(':')[0]
            community['value'] = ':'.join(item.split(':')[1:])
            body['spec']['communities'].append(
                community
            )

    if len(params['community']) == 0:
        while True:
            name = my_output.get_value('Community name', empty=True)
            if name is None or len(name) == 0:
                break

            value = my_output.get_value('Community value', empty=True)
            if value is None or len(value) == 0:
                break

            if len(value.split(':')) != 2:
                my_output.error('Community value format X:Y required')
                continue

            community = {}
            community['name'] = name
            community['value'] = value
            body['spec']['communities'].append(
                community
            )

    if len(body['spec']['communities']) == 0:
        return None
    
    return body


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - MetalLB Operator - Create community', before_newline=True, after_newline=True, double_underline=True)

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

    peers = params['k8s_handler'].get_communitys(cache_enabled=False)
    if peers is None:
        my_output.error('failed to get Community crds')
        return False
    
    k8s_output_handler.print_communitys(peers)
    my_output.default('')

    body = get_community_body(params, my_output)
    if body is None:
        return False
    
    success = params['k8s_handler'].create_or_update_community(
        body, 
        my_output=my_output, 
        confirmation=params['confirmation'], 
        wait=params['wait']
    )
    if not success:
        return False
    
    peers = params['k8s_handler'].get_communitys(cache_enabled=False)
    if peers is None:
        my_output.error('failed to get Community crds')
        return False
    
    k8s_output_handler.print_communitys(peers)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- MetalLB community defined')

    return True
