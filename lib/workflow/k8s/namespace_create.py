from lib import output_helper
from lib.workflow.k8s import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['labels', False, {}, 'dict', None, None, None, None],
        ['annotations', False, {}, 'dict', None, None, None, None],
        ['ovn-udn', False, False, 'bool', None, None, None, None],
        ['ovn-multicast', False, False, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params
        
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('Kubernetes Workflow - Namespace - Create', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['ovn-udn']:
        if params['namespace'].startswith('openshift-'):
            my_output.error('UDN mamespace cannot start with openshift-')
            return False
        
        params['labels']['k8s.ovn.org/primary-user-defined-network'] = ''
    
        namespace_mo = params['k8s_handler'].get_namespace(params['namespace'], return_mo=True, cache_enabled=False)
        if namespace_mo is not None:
            if not params['k8s_handler'].is_namespace_udn_enabled(managed_object=namespace_mo):
                my_output.error('UDN mamespace already exists and is not udn labeled')
                return False

    if params['ovn-multicast']:
        params['annotations']['k8s.ovn.org/multicast-enabled'] = 'true'
        
    success = params['k8s_handler'].create_namespace(
        params['namespace'],
        labels=params['labels'],
        annotations=params['annotations'],
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- namespace created')
    return True
