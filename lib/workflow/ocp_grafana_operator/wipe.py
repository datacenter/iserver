from lib import output_helper
from lib.workflow.ocp_grafana_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
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
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def wipe_grafana(params, my_output):
    my_output.default('Grafana', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_grafanas(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana(item['namespace'], item['name'], wait=True)
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def wipe_grafana_alert_group_rule(params, my_output):
    my_output.default('GrafanaAlertRuleGroup', before_newline=True, underline=True)
    managed_objects = params['k8s_handler'].get_grafana_alert_rule_groups(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False

    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana_alert_group_rule_mo(item['namespace'], item['name'])
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def wipe_grafana_contact_point(params, my_output):
    my_output.default('GrafanaContactPoint', before_newline=True, underline=True)            
    managed_objects = params['k8s_handler'].get_grafana_contact_points(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana_contact_point_mo(item['namespace'], item['name'])
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def wipe_grafana_dashboard(params, my_output):
    my_output.default('GrafanaDashboard', before_newline=True, underline=True)            
    managed_objects = params['k8s_handler'].get_grafana_dashboards(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False

    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana_dashboard_mo(item['namespace'], item['name'])
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def wipe_grafana_datasource(params, my_output):
    my_output.default('GrafanaDatasource', before_newline=True, underline=True)            
    managed_objects = params['k8s_handler'].get_grafana_datasources(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False
    
    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana_datasource_mo(item['namespace'], item['name'])
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def wipe_grafana_folder(params, my_output):
    my_output.default('GrafanaFolder', before_newline=True, underline=True)            
    managed_objects = params['k8s_handler'].get_grafana_folders(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False

    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana_folder_mo(item['namespace'], item['name'])
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def wipe_grafana_library_panel(params, my_output):
    my_output.default('GrafanaLibraryPanel', before_newline=True, underline=True)            
    managed_objects = params['k8s_handler'].get_grafana_library_panels(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False

    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana_library_panel_mo(item['namespace'], item['name'])
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def wipe_grafana_mute_timing(params, my_output):
    my_output.default('GrafanaMuteTiming', before_newline=True, underline=True)            
    managed_objects = params['k8s_handler'].get_grafana_mute_timings(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False

    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana_mute_timing_mo(item['namespace'], item['name'])
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def wipe_grafana_notification_policy(params, my_output):
    my_output.default('GrafanaNotificationPolicy', before_newline=True, underline=True)            
    managed_objects = params['k8s_handler'].get_grafana_notification_policies(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False

    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana_notification_policy_mo(item['namespace'], item['name'])
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def wipe_grafana_notification_policy_route(params, my_output):
    my_output.default('GrafanaNotificationPolicyRoute', before_newline=True, underline=True)            
    managed_objects = params['k8s_handler'].get_grafana_notification_policy_routes(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False

    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana_notification_policy_route_mo(item['namespace'], item['name'])
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def wipe_grafana_notification_template(params, my_output):
    my_output.default('GrafanaNotificationTemplate', before_newline=True, underline=True)            
    managed_objects = params['k8s_handler'].get_grafana_notification_templates(cache_enabled=False)
    if managed_objects is None:
        my_output.error('REST API failed')
        return False

    if len(managed_objects) == 0:
        my_output.default('- no resources found')

    if len(managed_objects) > 0:
        for item in managed_objects:
            my_output.default('- %s/%s' % (item['namespace'], item['name']))
            success = params['k8s_handler'].delete_grafana_notification_template_mo(item['namespace'], item['name'])
            if not success:
                my_output.error('REST API failed')
                return False
            
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Grafana Operator - Wipe Resources', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_grafana_subscription(params['namespace'], params['name']):
        my_output.error('Grafana Operator is not installed')
        return True
    
    if not wipe_grafana(params, my_output):
        return False
    
    if not wipe_grafana_alert_group_rule(params, my_output):
        return False

    if not wipe_grafana_contact_point(params, my_output):
        return False

    if not wipe_grafana_dashboard(params, my_output):
        return False

    if not wipe_grafana_datasource(params, my_output):
        return False

    if not wipe_grafana_folder(params, my_output):
        return False

    if not wipe_grafana_library_panel(params, my_output):
        return False

    if not wipe_grafana_mute_timing(params, my_output):
        return False

    if not wipe_grafana_notification_policy(params, my_output):
        return False

    if not wipe_grafana_notification_policy_route(params, my_output):
        return False

    if not wipe_grafana_notification_template(params, my_output):
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Grafana resources deleted')

    return True
