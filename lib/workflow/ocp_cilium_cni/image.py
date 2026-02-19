import time
from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow.ocp_cilium_cni import restart
from lib.workflow.ocp_cilium_cni import agent_version


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'url' not in params or params['url'] is None:
        return None, 'image url required'

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
        'url',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Image upgrade', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_cilium(params, my_output, install_plan_enforced=False):
        return False

    my_output.default('Check cilium agent runtime image')
    success = params['k8s_handler'].is_cilium_agent_pod_image_hash(
        params['url'].split(':')[1],
        cache_enabled=False
    )
    if success:
        my_output.default('Image already running')
        return True
    
    my_output.default('Image needs to be changed')

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['package'],
        csv_info=True,
        plan_info=True,
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Operator not found: %s' % (params['name']))
        return False

    local_common.print_subscription(my_output, subscription)

    csv = params['k8s_handler'].get_cluster_service_version_optimized(
        subscription['csv']['namespace'],
        subscription['csv']['name'],
        cache_enabled=False
    )
    if csv is None:
        my_output.error('Failed to get csv')
        my_output.default('Install plan may have been never approved')
        return False

    try:
        csv['image'] = csv['spec']['install']['spec']['deployments'][0]['spec']['template']['spec']['containers'][0]['image']
    except BaseException:
        my_output.error('Exception: failed to get container image from csv')
        return False

    local_common.print_csv(my_output, csv)

    if csv['image'] == params['url']:
        my_output.default('Cilium already running target image')

        cparams = {}
        cparams['cluster'] = params['cluster']
        cparams['check-verbose'] = False
        success = agent_version.run(cparams, log_id=log_id)
        if not success:
            return False

        return True

    body = {}
    body['apiVersion'] = 'operators.coreos.com/v1alpha1'
    body['kind'] = 'ClusterServiceVersion'
    body['metadata'] = {}
    body['metadata']['namespace'] = subscription['csv']['namespace']
    body['metadata']['name'] = subscription['csv']['name']

    csv_mo = params['k8s_handler'].get_cluster_service_version_optimized(
        subscription['csv']['namespace'],
        subscription['csv']['name'],
        cache_enabled=False,
        return_mo=True
    )
    body['spec'] = csv_mo['spec']
    try:
        body['spec']['install']['spec']['deployments'][0]['spec']['template']['spec']['containers'][0]['image'] = params['url']
    except BaseException:
        my_output.error('Unexpected csv body')
        return False
    
    success = params['k8s_handler'].patch_resource(
        body
    )
    if not success:
        my_output.error('REST API failed')
        return False

    my_output.default('CSV patched')

    csv = params['k8s_handler'].get_cluster_service_version_optimized(
        subscription['csv']['namespace'],
        subscription['csv']['name'],
        cache_enabled=False
    )
    if csv is None:
        my_output.error('Failed to get csv')
        return False

    try:
        csv['image'] = csv['spec']['install']['spec']['deployments'][0]['spec']['template']['spec']['containers'][0]['image']
    except BaseException:
        my_output.error('Exception: failed to get container image from csv')
        return False

    local_common.print_csv(my_output, csv)

    cparams = {}
    cparams['cluster'] = params['cluster']
    cparams['check-verbose'] = False
    success = restart.run(cparams, log_id=log_id)
    if not success:
        return False

    my_output.default('Take a nap [360s]...')
    time.sleep(360)

    cparams = {}
    cparams['cluster'] = params['cluster']
    cparams['check-verbose'] = False
    success = agent_version.run(cparams, log_id=log_id)
    if not success:
        return False
    
    return True
