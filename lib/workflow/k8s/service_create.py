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
        ['label', True, None, 'dict', None, None, None, None],
        ['selector', True, None, 'dict', None, None, None, None],
        ['type', False, None, 'str', None, None, ['NodePort'], None],
        ['port', False, None, 'list-of-dict', None, None, None, None]
    ]

    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params

    return local_common.sanitize_params(params, allowed_keys), None


def get_base_body(params):
    body = {}
    body['apiVersion'] = 'v1'
    body['kind'] = 'Service'
    body['metadata'] = {}
    body['metadata']['namespace'] = params['namespace']
    body['metadata']['name'] = params['name']
    body['spec'] = {}
    body['spec']['type'] = params['type']
    return body


def get_node_port_body(params):
    body = get_base_body(params)
    if params['label'] is not None and len(params['label']) > 0:
        body['metadata']['labels'] = params['label']
    if params['selector'] is not None and len(params['selector']) > 0:
        body['spec']['selector'] = params['selector']
    body['spec']['ports'] = []
    for item in params['port']:
        port_mo = {}
        if 'name' in item:
            port_mo['name'] = item['name']
        if 'protocol' in item:
            port_mo['protocol'] = item['protocol']
        if 'port' in item:
            port_mo['port'] = item['port']
        if 'targetPort' in item:
            port_mo['targetPort'] = item['targetPort']
        body['spec']['ports'].append(port_mo)
    return body


def get_load_balancer_body(params):
    body = get_base_body(params)
    if params['label'] is not None and len(params['label']) > 0:
        body['metadata']['labels'] = params['label']
    if params['selector'] is not None and len(params['selector']) > 0:
        body['spec']['selector'] = params['selector']
    body['spec']['ports'] = []
    for item in params['port']:
        port_mo = {}
        if 'name' in item:
            port_mo['name'] = item['name']
        if 'protocol' in item:
            port_mo['protocol'] = item['protocol']
        if 'port' in item:
            port_mo['port'] = item['port']
        if 'targetPort' in item:
            port_mo['targetPort'] = item['targetPort']
        body['spec']['ports'].append(port_mo)
    return body


def get_service_body(params):
    if params['type'] == 'NodePort':
        return get_node_port_body(params)    
    if params['type'] == 'LoadBalancer':
        return get_load_balancer_body(params) 
    return None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Service - Create', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    body = get_service_body(params)
    if body is None:
        my_output.error('Exception in processing input data')
        return False
    
    success = params['k8s_handler'].create_service(
        params['namespace'], 
        params['name'], 
        body,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=params['wait']
    )
    if not success:
        return False

    info = params['k8s_handler'].get_service(
        params['namespace'], 
        params['name'], 
        cache_enabled=False
    )
    k8s_output_handler.print_services([info])

    info = params['k8s_handler'].get_endpoint(
        params['namespace'], 
        params['name'], 
        cache_enabled=False
    )
    k8s_output_handler.print_endpoints([info])

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- service created')
    return True
