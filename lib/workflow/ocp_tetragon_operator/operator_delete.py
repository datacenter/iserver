import json
import yaml
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_tetragon_operator import common as local_common


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


def check_alert_rule(params, my_output):
    my_output.default('Alert Rule', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_alert_rules(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_sandbox_policy(params, my_output):
    my_output.default('Sandbox Policy', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_sandbox_policies(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_sandbox_policy_namespaced(params, my_output):
    my_output.default('Sandbox Policy Namespaced', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_sandbox_policies_namespaced(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_tetragon_network_policy(params, my_output):
    my_output.default('Tetragon Network Policy', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_tetragon_network_policies(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_tetragon_network_policy_namespaced(params, my_output):
    my_output.default('Tetragon Network Policy Namespaced', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_tetragon_network_policies_namespaced(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_tracing_policy(params, my_output):
    my_output.default('Tracing Policy', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_tracing_policies(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_tracing_policy_namespaced(params, my_output):
    my_output.default('Tracing Policy Namespaced', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_tracing_policies_namespaced(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
            
    return True


def check_resources(params, my_output):
    if not check_alert_rule(params, my_output):
        return False
    
    if not check_sandbox_policy(params, my_output):
        return False

    if not check_sandbox_policy_namespaced(params, my_output):
        return False

    if not check_tetragon_network_policy(params, my_output):
        return False

    if not check_tetragon_network_policy_namespaced(params, my_output):
        return False

    if not check_tracing_policy(params, my_output):
        return False

    if not check_tracing_policy_namespaced(params, my_output):
        return False
    
    return True


def delete_subscription(params, my_output):
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Subscription already deleted: %s' % (params['name']))
    else:
        if not check_resources(params, my_output):
            return False

        success = params['k8s_handler'].delete_tetragon_subscription(
            subscription['namespace'],
            subscription['name'],
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    success = params['k8s_handler'].delete_catalog_source(
        params['catalog-namespace'],
        params['catalog-name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    success= params['k8s_handler'].delete_config_map(
        params['cm-namespace'],
        params['cm-name'],
        my_output=my_output,
        wait=True
    )

    success= params['k8s_handler'].delete_config_map(
        params['operator-cm-namespace'],
        params['operator-cm-name'],
        my_output=my_output,
        wait=True
    )

    success= params['k8s_handler'].delete_service_monitor(
        params['sm-namespace'],
        params['sm-name'],
        my_output=my_output,
        wait=True
    )

    success= params['k8s_handler'].delete_service(
        params['sm-namespace'],
        params['sm-name'],
        my_output=my_output,
        wait=True
    )

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Tetragon Operator - Delete Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not delete_subscription(params, my_output):
        return False
    
    success = params['k8s_handler'].delete_operator_group(
        params['namespace'],
        params['name'],
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
        
    return True
