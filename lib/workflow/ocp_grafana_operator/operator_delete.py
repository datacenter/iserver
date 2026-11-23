import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_grafana_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def check_resources(params, my_output):
    my_output.default('Check Grafana resource', before_newline=True, underline=True)
    
    my_output.default('- Grafana')
    managed_objects = params['k8s_handler'].get_grafanas(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False

    my_output.default('- GrafanaAlertRuleGroup')
    managed_objects = params['k8s_handler'].get_grafana_alert_rule_groups(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False

    my_output.default('- GrafanaContactPoint')
    managed_objects = params['k8s_handler'].get_grafana_contact_points(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False

    my_output.default('- GrafanaDashboard')
    managed_objects = params['k8s_handler'].get_grafana_dashboards(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False

    my_output.default('- GrafanaDatasource')
    managed_objects = params['k8s_handler'].get_grafana_datasources(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False

    my_output.default('- GrafanaFolder')
    managed_objects = params['k8s_handler'].get_grafana_folders(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False

    my_output.default('- GrafanaLibraryPanel')
    managed_objects = params['k8s_handler'].get_grafana_library_panels(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False

    my_output.default('- GrafanaMuteTiming')
    managed_objects = params['k8s_handler'].get_grafana_mute_timings(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False

    my_output.default('- GrafanaNotificationPolicy')
    managed_objects = params['k8s_handler'].get_grafana_notification_policies(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False

    my_output.default('- GrafanaNotificationPolicyRoute')
    managed_objects = params['k8s_handler'].get_grafana_notification_policy_routes(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False

    my_output.default('- GrafanaNotificationTemplate')
    managed_objects = params['k8s_handler'].get_grafana_notification_templates(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    if len(managed_objects) > 0:
        my_output.error('CRDs exists. Clean it up first')
        return False
                            
    return True


def delete_subscription(params, my_output):
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Subscription already deleted: %s' % (params['__default__']['name']))
        return True

    if not check_resources(params, my_output):
        return False

    success = params['k8s_handler'].delete_grafana_subscription(
        subscription['namespace'],
        subscription['name'],
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    return True


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

    if not delete_subscription(params, my_output):
        return False
    
    success = params['k8s_handler'].delete_operator_group(
        params['__default__']['namespace'],
        params['__default__']['operator-group-name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    if params['__default__']['delete-namespace']:
        success = params['k8s_handler'].delete_namespace(
            params['__default__']['namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Grafana Operator deleted')
    my_output.default('- Operator group deleted')
    my_output.default('- Namespace deleted')

    return True
