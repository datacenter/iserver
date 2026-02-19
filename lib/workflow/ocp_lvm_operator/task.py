from lib.workflow.ocp_lvm_operator import operator_create
from lib.workflow.ocp_lvm_operator import cluster_create
from lib.workflow.ocp_lvm_operator import operator_delete
from lib.workflow.ocp_lvm_operator import cluster_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if not isinstance(task, dict):
        return None, 'lvm task definition in dict format required'
    
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'lvm.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_create.validate(task['operator'])
        if task['operator'] is None:
            return None, error
        
    if 'cluster' in task:
        if not isinstance(task['cluster'], dict):
            return None, 'lvm.cluster list required'
        
        task['cluster']['cluster'] = cluster_name
        task['cluster']['confirmation'] = confirmation
        task['cluster']['base_directory'] = cluster_settings['directory']
        task['cluster'], error = cluster_create.validate(task['cluster'])
        if task['cluster'] is None:
            return None, error
        
    new_task = {}
    allowed_keys = [
        'operator',
        'cluster'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for lvm task'
    
    return new_task, None


def run(task, log_id=None):
    if 'operator' in task:
        success = operator_create.run(
            task['operator'],
            log_id=log_id
        )
        if not success:
            return False
        
    if 'cluster' in task:
        success = cluster_create.run(
            task['cluster'],
            log_id=log_id
        )
        if not success:
            return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if not isinstance(task, dict):
        return None, 'lvm task definition in dict format required'
    
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'lvm.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator'], error = operator_delete.validate(task['operator'])
        if task['operator'] is None:
            return None, error
        
    if 'cluster' in task:
        if not isinstance(task['cluster'], dict):
            return None, 'lvm.cluster list required'
        
        task['cluster']['cluster'] = cluster_name
        task['cluster'], error = cluster_delete.validate(task['cluster'])
        if task['cluster'] is None:
            return None, error
        
    new_task = {}
    allowed_keys = [
        'operator',
        'cluster'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for lvm task'
    
    return new_task, None


def delete(task, log_id=None):
    if 'cluster' in task:
        success = cluster_delete.run(
            task['cluster'],
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
