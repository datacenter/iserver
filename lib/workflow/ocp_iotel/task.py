from lib.workflow.ocp_iotel import instance_create 
from lib.workflow.ocp_iotel import poller_create 
from lib.workflow.ocp_iotel import instance_delete
from lib.workflow.ocp_iotel import poller_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'instance' in task:
        if not isinstance(task['instance'], dict):
            return None, 'iotel.instance dict required'

        task['instance']['cluster'] = cluster_name
        task['instance']['base_directory'] = cluster_settings['directory']
        task['instance']['confirmation'] = confirmation
        task['instance'], error = instance_create.validate(task['instance'])
        if error is not None:
            return None, error

    if 'poller' in task:
        if not isinstance(task['poller'], dict):
            return None, 'iotel.poller dict required'

        task['poller']['cluster'] = cluster_name
        task['poller']['base_directory'] = cluster_settings['directory']
        task['poller']['confirmation'] = confirmation
        task['poller'], error = poller_create.validate(task['poller'], None)
        if error is not None:
            return None, error
                 
    new_task = {}
    allowed_keys = [
        'instance',
        'poller'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for iotel task'
    
    return new_task, None


def run(params, log_id=None):
    if 'instance' in params:
        success = instance_create.run(params['instance'], log_id=log_id)
        if not success:
            return False

    if 'poller' in params:
        success = poller_create.run(params['poller'], log_id=log_id)
        if not success:
            return False
                
    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'instance' in task:
        if not isinstance(task['instance'], dict):
            return None, 'iotel.instance dict required'

        task['instance']['cluster'] = cluster_name
        task['instance']['confirmation'] = confirmation
        task['instance'], error = instance_delete.validate(task['instance'])
        if error is not None:
            return None, error

    if 'poller' in task:
        if not isinstance(task['poller'], dict):
            return None, 'iotel.poller dict required'

        task['poller']['cluster'] = cluster_name
        task['poller']['confirmation'] = confirmation
        task['poller'], error = poller_delete.validate(task['poller'])
        if error is not None:
            return None, error
                
    new_task = {}
    allowed_keys = [
        'instance',
        'poller'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for iotel task'
    
    return new_task, None


def delete(params, log_id=None):   
    if 'poller' in params:
        success = poller_delete.run(params['poller'], log_id=log_id)
        if not success:
            return False
             
    if 'instance' in params:
        success = instance_delete.run(params['instance'], log_id=log_id)
        if not success:
            return False

    return True