from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', True, 'openshift-mtv', 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['source', False, None, 'str', None, None, None, None],
        ['destination', False, None, 'str', None, None, None, None],
        ['network', False, None, 'str', None, None, None, None],
        ['storage', False, False, 'str', None, None, None, None],
        ['vm', False, None, 'list-of-str', 1, None, None, None],
        ['type', False, None, 'str', None, None, ['cold', 'warm'], None],
        ['target', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create Migration Plan')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True

    my_output.default('Validation checks', before_newline=True)

    if params['k8s_handler'].is_plan(params['namespace'], params['name']):
        my_output.default('- migration plan %s already defined' %  (params['name']), before_newline=True)
        return True

    info = params['k8s_handler'].get_provider(params['namespace'], params['source'])
    if info is None:
        my_output.default('Provider %s %s' % (params['source'], my_output.add_color('not found', 'Red')))
        return False
    my_output.default('- provider %s %s' % (params['source'], my_output.add_color('found', 'Green')))

    info = params['k8s_handler'].get_provider(params['namespace'], params['destination'])
    if info is None:
        my_output.default('Provider %s %s' % (params['destination'], my_output.add_color('not found', 'Red')))
        return False
    my_output.default('- provider %s %s' % (params['destination'], my_output.add_color('found', 'Green')))

    info = params['k8s_handler'].get_network_map(params['namespace'], params['network'])
    if info is None:
        my_output.default('- network map %s %s' % (params['network'], my_output.add_color('not found', 'Red')))
        return False
    my_output.default('- network map %s %s' % (params['network'], my_output.add_color('found', 'Green')))

    info = params['k8s_handler'].get_storage_map(params['namespace'], params['storage'])
    if info is None:
        my_output.default('- storage map %s %s' % (params['storage'], my_output.add_color('not found', 'Red')))
        return False
    my_output.default('- storage map %s %s' % (params['storage'], my_output.add_color('found', 'Green')))

    if not params['k8s_handler'].is_namespace(params['target']):
        my_output.default('- target namespace %s %s' % (params['target'], my_output.add_color('not found', 'Red')))
        return False
    my_output.default('- target namespace %s %s' % (params['target'], my_output.add_color('found', 'Green')))

    success = params['k8s_handler'].create_plan(
        params['namespace'],
        params['name'],
        params['source'],
        params['destination'],
        params['network'],
        params['storage'],
        params['vm'],
        params['target'],
        params['type'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )

    plans = params['k8s_handler'].get_plans(
        object_filter=[
            'namespace:%s' % (params['namespace']),
            'name:%s' % (params['name'])
        ],
        cache_enabled=False
    )
    k8s_output_handler.print_plans_state(plans)

    if not success:
        return False        
        
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- migration plan created and ready to run')

    return True
