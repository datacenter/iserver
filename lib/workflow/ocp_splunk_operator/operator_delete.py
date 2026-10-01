from lib import output_helper
from lib.workflow.ocp_splunk_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


# def check_cluster_manager(params, my_output):
#     my_output.default('ClusterManager', before_newline=True, underline=True)
#     managed_objects = params['k8s_handler'].get_splunk_cluster_managers(cache_enabled=False)
#     if managed_objects is None:
#         my_output.error('REST API failed')
#         return False
    
#     if len(managed_objects) == 0:
#         my_output.default('- no resources found')

#     if len(managed_objects) > 0:
#         my_output.error('CRDs exists. Clean it up first')
#         return False
            
#     return True


# def check_cluster_master(params, my_output):
#     my_output.default('ClusterMaster', before_newline=True, underline=True)
#     managed_objects = params['k8s_handler'].get_splunk_cluster_masters(cache_enabled=False)
#     if managed_objects is None:
#         my_output.error('REST API failed')
#         return False
    
#     if len(managed_objects) == 0:
#         my_output.default('- no resources found')

#     if len(managed_objects) > 0:
#         my_output.error('CRDs exists. Clean it up first')
#         return False
            
#     return True


# def check_indexer_cluster(params, my_output):
#     my_output.default('IndexerCluster', before_newline=True, underline=True)
#     managed_objects = params['k8s_handler'].get_splunk_indexer_clusters(cache_enabled=False)
#     if managed_objects is None:
#         my_output.error('REST API failed')
#         return False
    
#     if len(managed_objects) == 0:
#         my_output.default('- no resources found')

#     if len(managed_objects) > 0:
#         my_output.error('CRDs exists. Clean it up first')
#         return False
            
#     return True


# def check_license_manager(params, my_output):
#     my_output.default('LicenseManager', before_newline=True, underline=True)
#     managed_objects = params['k8s_handler'].get_splunk_license_managers(cache_enabled=False)
#     if managed_objects is None:
#         my_output.error('REST API failed')
#         return False
    
#     if len(managed_objects) == 0:
#         my_output.default('- no resources found')

#     if len(managed_objects) > 0:
#         my_output.error('CRDs exists. Clean it up first')
#         return False
            
#     return True


# def check_license_master(params, my_output):
#     my_output.default('LicenseMaster', before_newline=True, underline=True)
#     managed_objects = params['k8s_handler'].get_splunk_license_masters(cache_enabled=False)
#     if managed_objects is None:
#         my_output.error('REST API failed')
#         return False
    
#     if len(managed_objects) == 0:
#         my_output.default('- no resources found')

#     if len(managed_objects) > 0:
#         my_output.error('CRDs exists. Clean it up first')
#         return False
            
#     return True


# def check_monitoring_console(params, my_output):
#     my_output.default('MonitoringConsole', before_newline=True, underline=True)
#     managed_objects = params['k8s_handler'].get_splunk_monitoring_consoles(cache_enabled=False)
#     if managed_objects is None:
#         my_output.error('REST API failed')
#         return False
    
#     if len(managed_objects) == 0:
#         my_output.default('- no resources found')

#     if len(managed_objects) > 0:
#         my_output.error('CRDs exists. Clean it up first')
#         return False
            
#     return True


# def check_search_head_cluster(params, my_output):
#     my_output.default('SearchHeadCluster', before_newline=True, underline=True)
#     managed_objects = params['k8s_handler'].get_splunk_search_head_clusters(cache_enabled=False)
#     if managed_objects is None:
#         my_output.error('REST API failed')
#         return False
    
#     if len(managed_objects) == 0:
#         my_output.default('- no resources found')

#     if len(managed_objects) > 0:
#         my_output.error('CRDs exists. Clean it up first')
#         return False
            
#     return True


# def check_standalone(params, my_output):
#     my_output.default('Standalone', before_newline=True, underline=True)
#     managed_objects = params['k8s_handler'].get_splunk_standalones(cache_enabled=False)
#     if managed_objects is None:
#         my_output.error('REST API failed')
#         return False
    
#     if len(managed_objects) == 0:
#         my_output.default('- no resources found')

#     if len(managed_objects) > 0:
#         my_output.error('CRDs exists. Clean it up first')
#         return False
            
#     return True


# def check_resources(params, my_output):
#     if not check_cluster_manager(params, my_output):
#         return False

#     if not check_cluster_master(params, my_output):
#         return False

#     if not check_indexer_cluster(params, my_output):
#         return False

#     if not check_license_manager(params, my_output):
#         return False

#     if not check_license_master(params, my_output):
#         return False
    
#     if not check_monitoring_console(params, my_output):
#         return False

#     if not check_search_head_cluster(params, my_output):
#         return False

#     if not check_standalone(params, my_output):
#         return False

#     return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Operator')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    params = ocp_common.get_operator(params, my_output)
    if params['subscription'] is not None:
        params = local_common.collect_state_info(params, my_output)

        my_output.dictionary_ng(
            'Splunk Custom Resources',
            params['summary'],
            [
                ['standalone', 'standalone'],
                ['cluster master', 'cluster_master'],
                ['cluster manager', 'cluster_manager'],
                ['indexer cluster', 'indexer_cluster'],
                ['license manager', 'license_manager'],
                ['license master', 'license_master'],
                ['monitoring console', 'monitoring_console'],
                ['search head cluster', 'search_head_cluster']
            ]
        )
    
        if params['summary']['resources']:
            my_output.error('Delete splunk operator resources first')
            return False
        
    success = params['k8s_handler'].delete_splunk_subscription_role_binding(
        params['__default__']['name'],
        params['__default__']['role-binding-name'],
        my_output=my_output
    )
    if not success:
        return False

    success = ocp_common.delete_operator(
        params,
        my_output
    )
    if not success:
        return False
        
    # subscription = global_common.get_subscription(
    #     params['k8s_handler'], 
    #     params['name'], 
    #     my_output=my_output
    # )
    # if subscription is not None:
    #     if not check_resources(params, my_output):
    #         return False

    #     success = params['k8s_handler'].delete_splunk_subscription(
    #         params['namespace'], 
    #         params['name'],
    #         my_output=my_output,
    #         wait=True
    #     )
    #     if not success:
    #         return False

    # success = params['k8s_handler'].delete_splunk_subscription_role_binding(
    #     params['name'],
    #     params['role-binding-name'],
    #     my_output=my_output
    # )
    # if not success:
    #     return False
        
    # success = params['k8s_handler'].delete_operator_group(
    #     params['namespace'], 
    #     params['operator-group-name'],
    #     my_output=my_output,
    #     wait=True
    # )
    # if not success:
    #     return False

    # if params['delete-namespace']:
    #     success = params['k8s_handler'].delete_namespace(
    #         params['namespace'],
    #         my_output=my_output,
    #         wait=True
    #     )
    #     if not success:
    #         return False
    
    # my_output.default('')
    # my_output.default('Completed tasks')
    # my_output.default('- Splunk resources checked')
    # my_output.default('- Subscription and csv deleted')
    # my_output.default('- Role binding deleted')
    # my_output.default('- Operator Group deleted')
    # if params['delete-namespace']:
    #     my_output.default('- Namespace deleted')

    return True
