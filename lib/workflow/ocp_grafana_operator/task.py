from lib.workflow.ocp_grafana_operator import operator_create
from lib.workflow.ocp_prometheus import monitoring_enable
from lib.workflow.ocp_grafana_operator import instance_create
from lib.workflow.ocp_grafana_operator import dashboard_create
from lib.workflow.ocp_grafana_operator import operator_delete
from lib.workflow.ocp_prometheus import monitoring_disable
from lib.workflow.ocp_grafana_operator import instance_delete
from lib.workflow.ocp_grafana_operator import wipe


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'grafana.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_create.validate(task['operator'])
        if error is not None:
            return None, error
        
    if 'mon' in task:
        if not isinstance(task['mon'], dict):
            return None, 'grafana.mon dict required'

        task['mon']['cluster'] = cluster_name
        task['mon']['confirmation'] = confirmation
        task['mon'], error = monitoring_enable.validate(task['mon'])
        if error is not None:
            return None, error

    if 'instance' in task:
        if not isinstance(task['instance'], list):
            return None, 'grafana.instance list required'

        for item in task['instance']:
            if not isinstance(item, dict):
                return None, 'grafana.instance list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item, error = instance_create.validate(item)
            if error is not None:
                return None, error

    if 'dashboard' in task:
        if not isinstance(task['dashboard'], list):
            return None, 'grafana.dashboard list required'

        for item in task['dashboard']:
            if not isinstance(item, dict):
                return None, 'grafana.dashboard list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item, error = dashboard_create.validate(item)
            if error is not None:
                return None, error
                                    
    new_task = {}
    allowed_keys = [
        'operator',
        'mon',
        'instance',
        'dashboard'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for grafana task'
    
    return new_task, None


def run(params, log_id=None):
    if 'operator' in params:
        success = operator_create.run(params['operator'], log_id=log_id)
        if not success:
            return False

    if 'mon' in params:
        success = monitoring_enable.run(params['mon'], log_id=log_id)
        if not success:
            return False

    if 'instance' in params:
        for item in params['instance']:
            success = instance_create.run(item, log_id=log_id)
            if not success:
                return False

    if 'dashboard' in params:
        for item in params['dashboard']:
            success = dashboard_create.run(item, log_id=log_id)
            if not success:
                return False
            
    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'grafana.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_delete.validate(task['operator'])
        if error is not None:
            return None, error

        if 'wipe' not in task:
            task['wipe'] = {}
            task['wipe']['cluster'] = cluster_name
            task['wipe'], error = wipe.validate(task['wipe'])
            if error is not None:
                return None, error
        
    if 'mon' in task:
        if not isinstance(task['mon'], dict):
            return None, 'grafana.mon dict required'

        task['mon']['cluster'] = cluster_name
        task['mon']['confirmation'] = confirmation
        task['mon'], error = monitoring_disable.validate(task['mon'])
        if error is not None:
            return None, error

    if 'instance' in task:
        if not isinstance(task['instance'], list):
            return None, 'grafana.instance list required'

        for item in task['instance']:
            if not isinstance(item, dict):
                return None, 'grafana.instance list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item, error = instance_delete.validate(item)
            if error is not None:
                return None, error

    if 'wipe' in task:
        if not isinstance(task['wipe'], dict):
            return None, 'grafana.wipe dict required'

        task['wipe']['cluster'] = cluster_name
        task['wipe']['confirmation'] = confirmation
        task['wipe'], error = wipe.validate(task['wipe'])
        if error is not None:
            return None, error


    new_task = {}
    allowed_keys = [
        'operator',
        'mon',
        'instance',
        'wipe'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for grafana task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'instance' in params:
        for item in params['instance']:
            success = instance_delete.run(item, log_id=log_id)
            if not success:
                return False

    if 'wipe' in params or 'operator' in params:
        success = wipe.run(params['wipe'], log_id=log_id)
        if not success:
            return False

    if 'mon' in params:
        success = monitoring_disable.run(params['mon'], log_id=log_id)
        if not success:
            return False

    if 'operator' in params:
        success = operator_delete.run(params['operator'], log_id=log_id)
        if not success:
            return False

    return True