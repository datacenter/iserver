from lib.workflow.ocp_vast_operator import operator_create
from lib.workflow.ocp_vast_operator import cluster_create
from lib.workflow.ocp_vast_operator import driver_create
from lib.workflow.ocp_vast_operator import storage_create
from lib.workflow.ocp_vast_operator import operator_delete
from lib.workflow.ocp_vast_operator import driver_delete
from lib.workflow.ocp_vast_operator import cluster_delete
from lib.workflow.ocp_vast_operator import storage_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if not isinstance(task, dict):
        return None, 'vast task definition in dict format required'
    
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'vast.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_create.validate(task['operator'])
        if task['operator'] is None:
            return None, error

    if 'driver' in task:
        if not isinstance(task['driver'], list):
            return None, 'vast.driver list required'
        
        for item in task['driver']:
            if not isinstance(item, dict):
                return None, 'vast.driver list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item, error = driver_create.validate(item)
            if item is None:
                return None, error

    if 'cluster' in task:
        if not isinstance(task['cluster'], list):
            return None, 'vast.cluster list required'
        
        for item in task['cluster']:
            if not isinstance(item, dict):
                return None, 'vast.cluster list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item, error = cluster_create.validate(item)
            if item is None:
                return None, error
        
    if 'storage' in task:
        if not isinstance(task['storage'], list):
            return None, 'vast.storage list required'
        
        for item in task['storage']:
            if not isinstance(item, dict):
                return None, 'vast.storage list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item, error = storage_create.validate(item)
            if item is None:
                return None, error

    new_task = {}
    allowed_keys = [
        'operator',
        'driver',
        'cluster',
        'storage'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for vast task'
    
    return new_task, None


def run(task, log_id=None):
    if 'operator' in task:
        success = operator_create.run(
            task['operator'],
            log_id=log_id
        )
        if not success:
            return False

    if 'driver' in task:
        for item in task['driver']:
            success = driver_create.run(
                item,
                log_id=log_id
            )
            if not success:
                return False
                    
    if 'cluster' in task:
        for item in task['cluster']:
            success = cluster_create.run(
                item,
                log_id=log_id
            )
            if not success:
                return False

    if 'storage' in task:
        for item in task['storage']:
            success = storage_create.run(
                item,
                log_id=log_id
            )
            if not success:
                return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if not isinstance(task, dict):
        return None, 'vast task definition in dict format required'
    
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'vast.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator'], error = operator_delete.validate(task['operator'])
        if task['operator'] is None:
            return None, error
        
    if 'driver' in task:
        if not isinstance(task['driver'], list):
            return None, 'vast.driver list required'
        
        for item in task['driver']:
            if not isinstance(item, dict):
                return None, 'vast.driver list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item, error = driver_delete.validate(item)
            if item is None:
                return None, error

    if 'cluster' in task:
        if not isinstance(task['cluster'], list):
            return None, 'vast.cluster list required'
        
        for item in task['cluster']:
            if not isinstance(item, dict):
                return None, 'vast.cluster list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item, error = cluster_delete.validate(item)
            if item is None:
                return None, error
        
    if 'storage' in task:
        if not isinstance(task['storage'], list):
            return None, 'vast.storage list required'
        
        for item in task['storage']:
            if not isinstance(item, dict):
                return None, 'vast.storage list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item, error = storage_delete.validate(item)
            if item is None:
                return None, error

    new_task = {}
    allowed_keys = [
        'operator',
        'driver',
        'cluster',
        'storage'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for vast task'
    
    return new_task, None


def delete(task, log_id=None):
    if 'storage' in task:
        for item in task['storage']:
            success = storage_delete.run(
                item,
                log_id=log_id
            )
            if not success:
                return False
            
    if 'cluster' in task:
        for item in task['cluster']:
            success = cluster_delete.run(
                item,
                log_id=log_id
            )
            if not success:
                return False

    if 'driver' in task:
        for item in task['driver']:
            success = driver_delete.run(
                item,
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
