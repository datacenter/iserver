from lib.workflow.ocp_prometheus import monitoring_enable
from lib.workflow.ocp_prometheus import monitoring_disable


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'user' in task:
        if not isinstance(task['user'], dict):
            return None, 'prometheus.user dict required'

        task['user']['cluster'] = cluster_name
        task['user']['confirmation'] = confirmation
        task['user'], error = monitoring_enable.validate(task['user'])
        if error is not None:
            return None, error
                        
    new_task = {}
    allowed_keys = [
        'user'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for prometheus task'
    
    return new_task, None


def run(params, log_id=None):
    if 'user' in params:
        success = monitoring_enable.run(params['user'], log_id=log_id)
        if not success:
            return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'user' in task:
        if not isinstance(task['user'], dict):
            return None, 'prometheus.mon dict required'

        task['user']['cluster'] = cluster_name
        task['user']['confirmation'] = confirmation
        task['user'], error = monitoring_disable.validate(task['user'])
        if error is not None:
            return None, error

    new_task = {}
    allowed_keys = [
        'user'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for prometheus task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'user' in params:
        success = monitoring_disable.run(params['user'], log_id=log_id)
        if not success:
            return False

    return True