import os
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_ai_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    params['instance'] = None

    if 'filename' in params:
        try:
            if not os.path.isabs(params['filename']):
                params['filename'] = os.path.join(
                    params['base_directory'],
                    params['filename']
                )
        except BaseException:
            return None, 'Instance file path detection failed'
        
        params['instance'] = file_helper.get_file_yaml(
            params['filename']
        )
        if params['instance'] is None:
            return None, 'Yaml file read failed: %s' % (params['filename'])
        
        if 'kind' not in params['instance'] or params['instance']['kind'] != 'DataScienceCluster':
            return None, 'Invalid yaml file content: %s' % (params['filename'])

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
        'instance',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


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
    my_output.default('OpenShift Workflow - Data Science (AI) - Create Data Science Cluster', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
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
        params['serverless'],
        return_mo=False,
        cache_enabled=False
    )
    if serverless_subscription is None:
        my_output.default('Operator not found: %s' % (params['serverless']))
        return False

    my_output.default('Serverless Operator', underline=True)
    my_output.default('- subscription: %s' % (serverless_subscription['namespace_name']))
    my_output.default('- channel: %s' % (serverless_subscription['channel']))
    my_output.default('- csv: %s' % (serverless_subscription['installed_csv']))

    mesh_subscription = params['k8s_handler'].get_subscription_by_package(
        params['mesh'],
        return_mo=False,
        cache_enabled=False
    )
    if mesh_subscription is None:
        my_output.default('Operator not found: %s' % (params['mesh']))
        return False

    my_output.default('Service Mesh Operator', underline=True)
    my_output.default('- subscription: %s' % (mesh_subscription['namespace_name']))
    my_output.default('- channel: %s' % (mesh_subscription['channel']))
    my_output.default('- csv: %s' % (mesh_subscription['installed_csv']))

    if params['instance'] is None:
        params['instance'] = params['k8s_handler'].get_ods_package_channel_example(
            subscription['spec']['channel'],
            'DataScienceCluster'
        )
        if params['instance'] is None:
            my_output.error('Failed to get DataScienceCluster reference example in channel %s' % (subscription['spec']['channel']))
            return False

        params['instance'] = fixup_dsc(params['instance'], my_output)
        if params['instance'] is None:
            return False

    success = params['k8s_handler'].create_data_science_cluster(
        params['instance'],
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
