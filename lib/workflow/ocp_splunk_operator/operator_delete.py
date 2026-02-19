import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_splunk_operator import common as local_common
from lib.workflow import ocp_common as global_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def check_cluster_manager(params, my_output):
    my_output.default('ClusterManager', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_splunk_cluster_managers(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_cluster_master(params, my_output):
    my_output.default('ClusterMaster', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_splunk_cluster_masters(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_indexer_cluster(params, my_output):
    my_output.default('IndexerCluster', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_splunk_indexer_clusters(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_license_manager(params, my_output):
    my_output.default('LicenseManager', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_splunk_license_managers(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_license_master(params, my_output):
    my_output.default('LicenseMaster', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_splunk_license_masters(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_monitoring_console(params, my_output):
    my_output.default('MonitoringConsole', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_splunk_monitoring_consoles(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_search_head_cluster(params, my_output):
    my_output.default('SearchHeadCluster', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_splunk_search_head_clusters(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_standalone(params, my_output):
    my_output.default('Standalone', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_splunk_standalones(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_resources(params, my_output):
    if not check_cluster_manager(params, my_output):
        return False

    if not check_cluster_master(params, my_output):
        return False

    if not check_indexer_cluster(params, my_output):
        return False

    if not check_license_manager(params, my_output):
        return False

    if not check_license_master(params, my_output):
        return False
    
    if not check_monitoring_console(params, my_output):
        return False

    if not check_search_head_cluster(params, my_output):
        return False

    if not check_standalone(params, my_output):
        return False

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Splunk Operator - Delete Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    subscription = global_common.get_subscription(
        params['k8s_handler'], 
        params['name'], 
        my_output=my_output
    )
    if subscription is not None:
        if not check_resources(params, my_output):
            return False

        success = params['k8s_handler'].delete_splunk_subscription(
            params['namespace'], 
            params['name'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    success = params['k8s_handler'].delete_splunk_subscription_role_binding(
        params['name'],
        params['role-binding-name'],
        my_output=my_output
    )
    if not success:
        return False
        
    success = params['k8s_handler'].delete_operator_group(
        params['namespace'], 
        params['operator-group-name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    if params['delete-namespace']:
        success = params['k8s_handler'].delete_namespace(
            params['namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Splunk resources checked')
    my_output.default('- Subscription and csv deleted')
    my_output.default('- Role binding deleted')
    my_output.default('- Operator Group deleted')
    if params['delete-namespace']:
        my_output.default('- Namespace deleted')

    return True
