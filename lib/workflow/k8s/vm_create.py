from lib import ip_helper
from lib import output_helper
from lib.workflow.k8s import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['template', True, None, 'str', None, None, ['c8kv'], None],
        ['node', True, None, 'str', None, None, None, None],
        ['sc', True, None, 'str', None, None, None, None],
        ['url', True, None, 'str', None, None, None, None],
        ['pvc', True, None, 'k8s', None, None, None, None],
        ['size', True, None, 'str', None, None, None, None],
        ['cores', True, None, 'int', 1, 16, None, None],
        ['threads', True, None, 'int', 1, 16, None, None],
        ['sockets', True, None, 'int', 1, 16, None, None],
        ['day0', True, None, 'str', None, None, None, None],
        ['interface', True, None, 'list-of-dict', None, None, None, None],
        ['selector', True, None, 'dict', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params

    return local_common.sanitize_params(params, allowed_keys), None


def get_variables(params, my_output):
    variables = {}
    for key in ['node', 'day0', 'url', 'pvc', 'size', 'sc', 'cores', 'threads', 'sockets', 'interface', 'selector']:
        if params[key] is not None:
            variables[key] = params[key]

    if 'url' in variables:
        if not ip_helper.is_url_accessible(variables['url']):
            my_output.error('url not accessible: %s' % (variables['url']))
            return None
        
    if 'pvc' in variables:
        if len(variables['pvc'].split('/')) == 1:
            pvc_namespace = params['namespace']
            pvc_name = variables['pvc']
        else:
            (pvc_namespace, pvc_name) = variables['pvc'].split('/')
        
        if not params['k8s_handler'].is_pvc(pvc_namespace, pvc_name, cache_enabled=False):
            my_output.error('pvc not found: %s/%s' % (pvc_namespace, pvc_name))
            return None

        variables['pvc'] = '%s/%s' % (pvc_namespace, pvc_name)
        
    if 'url' not in variables and 'pvc' not in variables:
        my_output.error('url or pvc attribute required')
        return None

    if 'sc' in variables:
        sc_name = variables['sc']
        variables['sc'] = params['k8s_handler'].get_storage_class(sc_name, cache_enabled=False)
        if variables['sc'] is None:
            my_output.error('user-defined service class not found: %s' % (sc_name))
            return None
    else:
        variables['sc'] = params['k8s_handler'].get_default_storage_class(fallback_to_single=True, cache_enabled=False)
        if variables['sc'] is None:
            my_output.error('default or explicit service class required')
            return None
    
    variables['clone'] = False
    if variables['sc']['csiType'] is not None:
        if variables['sc']['csiType'] in ['ODF']:
            variables['clone'] = True

    if 'node' in variables:
        if not params['k8s_handler'].is_node(variables['node'], cache_enabled=False):
            my_output.error('node not found: %s' % (variables['node']))
            return None
        
    return variables


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('Kubernetes Workflow - Virtual Machine - Create', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['template'] is not None:
        variables = get_variables(params, my_output)
        if variables is None:
            return False
        
        success = params['k8s_handler'].create_virtual_machine_template(
            params['namespace'], 
            params['name'], 
            params['template'], 
            variables,
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True        
        )
        if not success:
            return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- virtual machine created')
    return True
