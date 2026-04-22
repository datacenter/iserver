import time
from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow.ocp_cilium_cni import restart
from lib.workflow.ocp_cilium_cni import agent_version
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['url', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Image upgrade', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False

    my_output.default('Check cilium agent runtime image', before_newline=True)
    success = params['k8s_handler'].is_cilium_agent_pod_image_hash(
        params['url'].split(':')[1],
        cache_enabled=False
    )
    if success:
        my_output.default('Image already running')
        return True
    
    my_output.default('Image needs to be changed')

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['package'],
        csv_info=True,
        plan_info=True,
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Operator not found: %s' % (params['name']))
        return False

    local_common.print_subscription(my_output, subscription)

    csv = params['k8s_handler'].get_cluster_service_version(
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

    csv_mo = params['k8s_handler'].get_cluster_service_version(
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

    csv = params['k8s_handler'].get_cluster_service_version(
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
    success = agent_version.run(cparams, log_id=log_id)
    if not success:
        return False
    
    return True
