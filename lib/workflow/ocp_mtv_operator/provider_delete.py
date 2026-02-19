from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'provider_name' not in params:
        params['provider_name'] = None

    if 'confirmation' not in params:
        params['confirmation'] = True

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
        'provider_name',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Provider', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True

    object_filter = []
    if params['provider_name'] is not None:
        object_filter.append('name:%s' % (params['provider_name']))

    providers = params['k8s_handler'].get_providers(
        object_filter=object_filter, 
        network_info=True,
        storage_info=True,
        skip_host=True,
        plan_info=True, 
        cache_enabled=False
    )
    if providers is None:
        my_output.error('Failed to get providers')
        return False
    
    if len(providers) == 0:
        my_output.default('No providers defined')
        return True
    
    k8s_output_handler.print_providers(providers)

    if params['confirmation']:
        if not get_confirmation():
            return False
    
    used = []
    for provider in providers:
        if provider['used']:
            used.append(
                provider['name']
            )

    if len(used) > 0:
        my_output.my_list(
            used,
            title='Providers being used and not to be deleted',
            underline=False,
            before_newline=True,
            ending_newline=True
        )

    for provider in providers:
        if provider['used']:
            continue

        success = params['k8s_handler'].delete_provider(
            provider['namespace'],
            provider['name'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- selected providers deleted')
    if len(used) > 0:
        my_output.default('- providers used by maps or migration plans not deleted')

    return True
