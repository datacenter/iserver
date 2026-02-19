import os
import uuid
from lib import file_helper
from lib import ip_helper
from lib import output_helper
from lib.workflow.ocp_gpu_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'confirmation' not in params:
        params['confirmation'] = False

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
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - GPU Operator - Create DCGM Dashboard', before_newline=True, after_newline=True, double_underline=True)
    
    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False
    
    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
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
        params['monitoring']['dashboard_namespace'],
        params['monitoring']['dashboard_name'],
        cache_enabled=False
    )
    if is_config_map:
        my_output.default(
            'Monitoring dashboard config map already exists: %s/%s' % (
                params['monitoring']['dashboard_namespace'],
                params['monitoring']['dashboard_name']
            )
        )
        return True

    my_output.default('Monitoring dashboard source: %s' % (params['monitoring']['dashboard_url']), before_newline=True, after_newline=True)
    
    filename = os.path.join('/tmp', str(uuid.uuid4()))
    result = ip_helper.download_url(
        params['monitoring']['dashboard_url'],
        filename
    )
    if result is None:
        my_output.error('Failed to download dashboard: %s' % (params['monitoring']['dashboard_url']))
        return False

    content = file_helper.get_file_text(filename)
    if content is None:
        my_output.error('Failed to read downloaded file: %s' % (filename))
        return False

    my_output.default('Dashboard content downloaded from url: %s' % (params['monitoring']['dashboard_url']))

    labels = {}
    if params['monitoring']['admin']:
        labels['console.openshift.io/dashboard'] = "true"
        my_output.default('ConfigMap admin label: console.openshift.io/dashboard=true')

    if params['monitoring']['developer']:
        labels['console.openshift.io/odc-dashboard'] = "true"
        my_output.default('ConfigMap admin label: console.openshift.io/odc-dashboard=true')

    success = params['k8s_handler'].create_config_map_data_mo(
        params['monitoring']['dashboard_namespace'],
        params['monitoring']['dashboard_name'],
        'dcgm-exporter-dashboard.json',
        content,
        labels=labels
    )
    if not success:
        my_output.error('Failed to create config map with dashboard content')
        return False

    my_output.default('Config map create with dashboard content: %s/%s' % (
        params['monitoring']['dashboard_namespace'],
        params['monitoring']['dashboard_name']
    ))

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- GPU Monitoring Dashboard created')

    return True
