import yaml
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

    if 'node' not in params:
        params['node'] = None

    if 'app' not in params or params['app'] is None:
        return None, 'Application type required'

    if params['app'] not in ['netshoot']:
        return None, 'Unsupported app type'

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
        'node',
        'app',
        'wait',
        'verbose',
        'check-verbose',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def get_base_body(params):
    body = {}
    body['apiVersion'] = 'v1'
    body['kind'] = 'Pod'
    body['metadata'] = {}
    body['metadata']['namespace'] = params['namespace']
    body['metadata']['name'] = params['name']
    if len(params['label']) > 0:
        body['metadata']['labels'] = params['label']
    body['spec'] = {}
    body['spec']['containers'] = []
    if params['node'] is not None:
        body['spec']['nodeName'] = params['node']  
    return body


def get_netshoot_body(params):
    container_mo = {}
    container_mo['command'] = ['sleep', 'infinite']
    container_mo['image'] = 'nicolaka/netshoot:latest'
    container_mo['securityContext'] = {}
    container_mo['securityContext']['runAsUser'] = 0
    container_mo['securityContext']['capabilities'] = {}
    container_mo['securityContext']['capabilities']['add'] = ['IPC_LOCK', 'SYS_RESOURCE', 'NET_RAW']
    container_mo['name'] = 'netshoot'

    body = get_base_body(params)
    body['spec']['containers'].append(container_mo)
    return body


def get_pod_body(params):
    if params['app'] == 'netshoot':
        return get_netshoot_body(params)    
    return None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Pod - Create', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    body = get_pod_body(params)
    if body is None:
        my_output.error('Exception in processing input data')
        return False
    
    success = params['k8s_handler'].create_pod(
        params['namespace'], 
        params['name'], 
        body,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=params['wait']
    )
    if not success:
        return False

    info = params['k8s_handler'].get_pod(
        params['namespace'], 
        params['name'], 
        cache_enabled=False
    )
    k8s_output_handler.print_pods_state([info])
    return True
