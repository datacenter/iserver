from lib.workflow.ocp_cert_manager import feature_enable
from lib.workflow.ocp_cert_manager import feature_disable


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'feature' in task:
        if not isinstance(task['feature'], dict):
            return None, 'cilium_pnet.feature dict required'

        task['feature']['cluster'] = cluster_name
        task['feature']['confirmation'] = confirmation
        task['feature'], error = feature_enable.validate(task['feature'])
        if error is not None:
            return None, error

    new_task = {}
    allowed_keys = [
        'feature'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for cilium_pnet task'
    
    return new_task, None


def run(params, log_id=None):
    if 'feature' in params:
        success = feature_enable.run(params['feature'], log_id=log_id)
        if not success:
            return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'feature' in task:
        if not isinstance(task['feature'], dict):
            return None, 'cert_manager.feature dict required'

        task['feature']['cluster'] = cluster_name
        task['feature']['confirmation'] = confirmation
        task['feature'], error = feature_disable.validate(task['feature'])
        if error is not None:
            return None, error

    new_task = {}
    allowed_keys = [
        'feature'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for cilium_pnet task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'feature' in params:
        success = feature_disable.run(params['feature'], log_id=log_id)
        if not success:
            return False

    return True