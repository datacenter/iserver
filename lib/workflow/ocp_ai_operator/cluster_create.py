import os
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_ai_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['filename', True, None, 'file-k8s', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def fixup_dsc(dsc, my_output):
    try:
        for component in dsc['spec']['components']:
            if 'managementState' in dsc['spec']['components'][component]:
                dsc['spec']['components'][component]['managementState'] = 'Managed'

            if component == 'kserver':
                dsc['spec']['components']['kserve']['nim']['managementState'] = 'Managed'
                dsc['spec']['components']['kserve']['serving']['managementState'] = 'Managed'
    except BaseException:
        my_output.error('Unexpected DataScienceCluster body')
        return None
    
    return dsc


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create Cluster')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Data Science (AI) Operator must be installed first')
        return False

    my_output.default('AI Operator', underline=True)
    my_output.default('- subscription: %s' % (subscription['namespace_name']))
    my_output.default('- channel: %s' % (subscription['channel']))
    my_output.default('- csv: %s' % (subscription['installed_csv']))

    if params['k8s_handler'].is_any_data_science_cluster(cache_enabled=False):
        my_output.default('Data science cluster already defined')
        return True

    serverless_subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['serverless'],
        return_mo=False,
        cache_enabled=False
    )
    if serverless_subscription is None:
        my_output.default('Operator not found: %s' % (params['__default__']['serverless']))
        return False

    my_output.default('Serverless Operator', underline=True)
    my_output.default('- subscription: %s' % (serverless_subscription['namespace_name']))
    my_output.default('- channel: %s' % (serverless_subscription['channel']))
    my_output.default('- csv: %s' % (serverless_subscription['installed_csv']))

    mesh_subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['mesh'],
        return_mo=False,
        cache_enabled=False
    )
    if mesh_subscription is None:
        my_output.default('Operator not found: %s' % (params['__default__']['mesh']))
        return False

    my_output.default('Service Mesh Operator', underline=True)
    my_output.default('- subscription: %s' % (mesh_subscription['namespace_name']))
    my_output.default('- channel: %s' % (mesh_subscription['channel']))
    my_output.default('- csv: %s' % (mesh_subscription['installed_csv']))

    instance_body = None
    if params['filename'] is not None:
        instance_body = file_helper.get_file_yaml(
            params['filename']
        )
        if instance_body is None:
            my_output.error('Failed to get data science cluster instance: %s' % (params['filename']))
            return False

    if instance_body is None:
        instance_body = params['k8s_handler'].get_ods_package_channel_example(
            subscription['spec']['channel'],
            'DataScienceCluster'
        )        
        if instance_body is None:
            my_output.error('Failed to get DataScienceCluster reference example in channel %s' % (subscription['spec']['channel']))
            return False

        instance_body = fixup_dsc(instance_body, my_output)
        if params['instance'] is None:
            return False

    success = params['k8s_handler'].create_data_science_cluster(
        instance_body,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Data Science Cluster created')

    return True