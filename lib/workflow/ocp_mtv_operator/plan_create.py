from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'plan' not in params:
        return None, 'Map name required'
    
    if 'source' not in params:
        return None, 'Source name required'

    if 'destination' not in params:
        return None, 'Destination name required'

    if 'network' not in params:
        return None, 'Network map name required'

    if 'storage' not in params:
        return None, 'Storage map name required'

    if 'vm' not in params:
        return None, 'VM list required'

    if not isinstance(params['vm'], list):
        return None, 'VM list required'

    if 'type' not in params:
        return None, 'Migration type required'

    if params['type'] not in ['cold', 'warm']:
        return None, 'Unsupported migration type'
    
    if 'target' not in params:
        return None, 'Target namespace required'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'wait' not in params:
        params['wait'] = True

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'plan',
        'source',
        'destination',
        'network',
        'storage',
        'vm',
        'type',
        'target',
        'wait',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Migration Toolkit for Virtualization Operator - Create Migration Plan', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True

    my_output.default('Validation checks', before_newline=True)

    if params['k8s_handler'].is_plan(params['namespace'], params['plan']):
        my_output.default('- migration plan %s already defined' %  (params['plan']), before_newline=True)
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
        params['plan'],
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
            'name:%s' % (params['plan'])
        ],
        cache_enabled=False
    )
    k8s_output_handler.print_plans(plans)

    if not success:
        return False        
        
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- migration plan created and ready to run')

    return True
