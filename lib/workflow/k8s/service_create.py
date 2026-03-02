from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.k8s import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if '__id__' not in params:
        params['__id__'] = None

    if 'namespace' not in params or params['namespace'] is None:
        return None, 'Namespace required'

    if 'name' not in params or params['name'] is None:
        return None, 'Name required'

    if params['name'].endswith('-') and params['__id__'] is not None:
        params['name'] = '%s%s' % (
            params['name'],
            params['__id__']
        )

    if 'label' not in params:
        params['label'] = {}

    if not isinstance(params['label'], dict):
        return None, 'label dict required'
    
    for key in params['label']:
        if params['label'][key].endswith('-') and params['__id__'] is not None:
            params['label'][key] = '%s%s' % (
                params['label'][key],
                params['__id__']
            )

    if 'selector' not in params:
        params['selector'] = {}

    if not isinstance(params['selector'], dict):
        return None, 'selector dict required'
    
    for key in params['selector']:
        if params['selector'][key].endswith('-') and params['__id__'] is not None:
            params['selector'][key] = '%s%s' % (
                params['selector'][key],
                params['__id__']
            )

    if 'type' not in params or params['type'] is None:
        return None, 'Type required'

    if 'port' not in params or params['port'] is None:
        params['port'] = []

    if not isinstance(params['port'], list):
        return None, 'port list required'

    if len(params['port']) == 0:
        return None, 'port list with members required'

    for item in params['port']:
        if not isinstance(item, dict):
            return None, 'port list of dict required'

        keys = ['name', 'port', 'target']
        for key in keys:
            if key not in item:
                return None, 'port item with key %s required' % (key)

    if 'wait' not in params:
        params['wait'] = True

    if not isinstance(params['wait'], bool):
        return None, 'wait param must be true or false'
    
    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    allowed_keys = [
        'cluster',
        '__id__',
        'namespace',
        'name',
        'label',
        'selector',
        'type',
        'port',
        'wait',
        'verbose',
        'check-verbose',
        'confirmation'
    ]
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
    if len(params['label']) > 0:
        body['metadata']['labels'] = params['label']
    if len(params['selector']) > 0:
        body['spec']['selector'] = params['selector']
    body['spec']['ports'] = []
    for item in params['port']:
        port_mo = {}
        port_mo['name'] = item['name']
        port_mo['port'] = item['port']
        port_mo['targetPort'] = item['target']
        body['spec']['ports'].append(port_mo)
    return body


def get_load_balancer_body(params):
    body = get_base_body(params)
    if len(params['label']) > 0:
        body['metadata']['labels'] = params['label']
    if len(params['selector']) > 0:
        body['spec']['selector'] = params['selector']
    body['spec']['ports'] = []
    for item in params['port']:
        port_mo = {}
        port_mo['name'] = item['name']
        port_mo['port'] = item['port']
        port_mo['targetPort'] = item['target']
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
    return True
