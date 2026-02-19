from lib.workflow.ocp_sriov_operator import operator_create
from lib.workflow.ocp_sriov_operator import instance_create
from lib.workflow.ocp_sriov_operator import operator_delete
from lib.workflow.ocp_sriov_operator import instance_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if not isinstance(task, dict):
        return None, 'sriov task definition in dict format required'
    
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'sriov.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_create.validate(task['operator'])
        if task['operator'] is None:
            return None, error
        
    if 'instance' in task:
        if not isinstance(task['instance'], dict):
            return None, 'sriov.instance dict required'
        
        task['instance']['cluster'] = cluster_name
        task['instance']['confirmation'] = confirmation
        task['instance'], error = instance_create.validate(task['instance'])
        if task['instance'] is None:
            return None, error
        
    new_task = {}
    allowed_keys = [
        'operator',
        'instance'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for sriov task'
    
    return new_task, None


def run(task, log_id=None):
    if 'operator' in task:
        success = operator_create.run(
            task['operator'],
            log_id=log_id
        )
        if not success:
            return False
        
    if 'instance' in task:
        success = instance_create.run(
            task['instance'],
            log_id=log_id
        )
        if not success:
            return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if not isinstance(task, dict):
        return None, 'sriov task definition in dict format required'
    
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'sriov.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator'], error = operator_delete.validate(task['operator'])
        if task['operator'] is None:
            return None, error
        
    if 'instance' in task:
        if not isinstance(task['instance'], dict):
            return None, 'sriov.instance dict required'
        
        task['instance']['cluster'] = cluster_name
        task['instance'], error = instance_delete.validate(task['instance'])
        if task['instance'] is None:
            return None, error
        
    new_task = {}
    allowed_keys = [
        'operator',
        'instance'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for sriov task'
    
    return new_task, None


def delete(task, log_id=None):
    if 'instance' in task:
        success = instance_delete.run(
            task['instance'],
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
