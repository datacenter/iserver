import copy
from lib.workflow.ocp_local_storage_operator import operator_create
from lib.workflow.ocp_local_storage_operator import operator_delete
from lib.workflow.ocp_local_storage_operator import volume_create
from lib.workflow.ocp_local_storage_operator import volume_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'lso.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_create.validate(task['operator'])
        if task['operator'] is None:
            return None, error
        
    if 'volume' in task:
        if not isinstance(task['volume'], dict):
            return None, 'lso.volume dict required'
        
        task['volume']['cluster'] = cluster_name
        task['volume']['confirmation'] = confirmation
        new_volume, error = volume_create.validate(task['operator'])
        if new_volume is None:
            return None, error
        
    new_task = {}
    allowed_keys = [
        'operator',
        'volume'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for lso task'
    
    return new_task, None


def run(task, log_id=None):
    if 'operator' in task:
        success = operator_create.run(
            task['operator'],
            log_id=log_id
        )
        if not success:
            return False
        
    if 'volume' in task:
        success = volume_create.run(
            task['volume'],
            log_id=log_id
        )
        if not success:
            return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if not isinstance(task, dict):
        return None, 'lso task definition in dict format required'
    
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'lso.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator'], error = operator_delete.validate(task['operator'])
        if task['operator'] is None:
            return None, error

    if 'volume' in task:
        if not isinstance(task['volume'], dict):
            return None, 'lso.volume dict required'

        task['volume']['cluster'] = cluster_name
        task['volume'], error = volume_delete.validate(task['operator'])
        if task['operator'] is None:
            return None, error
                
    new_task = {}
    allowed_keys = [
        'operator',
        'volume'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for lso task'
    
    return new_task, None

def delete(task, log_id=None):
    if 'volume' in task:
        success = volume_delete.run(
            task['volume'],
            log_id=log_id
        )
        if not success:
            return False

    if 'operator' in task:
        success = operator_delete.run(
            task['operator'],
            log_id=log_id
        )
        if not success:
            return False

    return True
