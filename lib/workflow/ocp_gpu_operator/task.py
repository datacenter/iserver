from lib.workflow.ocp_gpu_operator import operator_create
from lib.workflow.ocp_gpu_operator import operator_delete
from lib.workflow.ocp_gpu_operator import policy_create
from lib.workflow.ocp_gpu_operator import policy_delete
from lib.workflow.ocp_gpu_operator import dashboard_create
from lib.workflow.ocp_gpu_operator import dashboard_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'gpu.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_create.validate(task['operator'])
        if error is not None:
            return None, error

    if 'policy' in task:
        if not isinstance(task['policy'], dict):
            return None, 'gpu.policy dict required'

        task['policy']['cluster'] = cluster_name
        task['policy']['confirmation'] = confirmation
        task['policy']['base_directory'] = cluster_settings['directory']
        task['policy'], error = policy_create.validate(task['policy'])
        if error is not None:
            return None, error

    if 'dashboard' in task:
        if not isinstance(task['dashboard'], dict):
            return None, 'gpu.dashboard dict required'

        task['dashboard']['cluster'] = cluster_name
        task['dashboard']['confirmation'] = confirmation
        task['dashboard'], error = dashboard_create.validate(task['dashboard'])
        if error is not None:
            return None, error
         
    new_task = {}
    allowed_keys = [
        'operator',
        'policy',
        'dashboard'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for gpu task'
    
    return new_task, None


def run(params, log_id=None):
    if 'operator' in params:
        success = operator_create.run(params['operator'], log_id=log_id)
        if not success:
            return False

    if 'policy' in params:
        success = policy_create.run(params['policy'], log_id=log_id)
        if not success:
            return False

    if 'dashboard' in params:
        success = dashboard_create.run(params['dashboard'], log_id=log_id)
        if not success:
            return False
        
    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'gpu.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator'], error = operator_delete.validate(task['operator'])
        if error is not None:
            return None, error

    if 'policy' in task:
        if not isinstance(task['policy'], dict):
            return None, 'gpu.policy dict required'

        task['policy']['cluster'] = cluster_name
        task['policy'], error = policy_delete.validate(task['policy'])
        if error is not None:
            return None, error
        
    if 'dashboard' in task:
        if not isinstance(task['dashboard'], dict):
            return None, 'gpu.dashboard dict required'

        task['dashboard']['cluster'] = cluster_name
        task['dashboard'], error = dashboard_delete.validate(task['dashboard'])
        if error is not None:
            return None, error
        
    new_task = {}
    allowed_keys = [
        'operator',
        'policy',
        'dashboard'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for gpu task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'dashboard' in params:
        success = dashboard_delete.run(params['dashboard'], log_id=log_id)
        if not success:
            return False
        
    if 'policy' in params:
        success = policy_delete.run(params['policy'], log_id=log_id)
        if not success:
            return False
        
    if 'operator' in params:
        success = operator_delete.run(params['operator'], log_id=log_id)
        if not success:
            return False

    return True