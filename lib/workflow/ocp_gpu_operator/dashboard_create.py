import os
import uuid
from lib import file_helper
from lib import ip_helper
from lib import output_helper
from lib.workflow.ocp_gpu_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create DCGM Dashboard')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.error('GPU Operator not installed')
        return False

    if not params['k8s_handler'].is_any_cluster_policy(cache_enabled=False):
        my_output.error('No NVIDIA Cluster Policy found')
        return False

    is_config_map = params['k8s_handler'].is_config_map(
        params['__default__']['monitoring']['dashboard_namespace'],
        params['__default__']['monitoring']['dashboard_name'],
        cache_enabled=False
    )
    if is_config_map:
        my_output.default(
            'Monitoring dashboard config map already exists: %s/%s' % (
                params['__default__']['monitoring']['dashboard_namespace'],
                params['__default__']['monitoring']['dashboard_name']
            )
        )
        return True

    my_output.default('Monitoring dashboard source: %s' % (params['__default__']['monitoring']['dashboard_url']), before_newline=True, after_newline=True)
    
    filename = os.path.join('/tmp', str(uuid.uuid4()))
    result = ip_helper.download_url(
        params['__default__']['monitoring']['dashboard_url'],
        filename
    )
    if result is None:
        my_output.error('Failed to download dashboard: %s' % (params['__default__']['monitoring']['dashboard_url']))
        return False

    content = file_helper.get_file_text(filename)
    if content is None:
        my_output.error('Failed to read downloaded file: %s' % (filename))
        return False

    my_output.default('Dashboard content downloaded from url: %s' % (params['__default__']['monitoring']['dashboard_url']))

    labels = {}
    if params['__default__']['monitoring']['admin']:
        labels['console.openshift.io/dashboard'] = "true"
        my_output.default('ConfigMap admin label: console.openshift.io/dashboard=true')

    if params['__default__']['monitoring']['developer']:
        labels['console.openshift.io/odc-dashboard'] = "true"
        my_output.default('ConfigMap admin label: console.openshift.io/odc-dashboard=true')

    data = {}
    data['dcgm-exporter-dashboard.json'] = content

    success = params['k8s_handler'].create_config_map(
        params['__default__']['monitoring']['dashboard_namespace'],
        params['__default__']['monitoring']['dashboard_name'],
        data,
        labels=labels
    )
    if not success:
        my_output.error('Failed to create config map with dashboard content')
        return False

    my_output.default('Config map create with dashboard content: %s/%s' % (
        params['__default__']['monitoring']['dashboard_namespace'],
        params['__default__']['monitoring']['dashboard_name']
    ))

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- GPU Monitoring Dashboard created')

    return True