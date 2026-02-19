from lib.workflow.ocp_splunk_operator import operator_create
from lib.workflow.ocp_splunk_operator import operator_delete
from lib.workflow.ocp_splunk_operator import instance_create
from lib.workflow.ocp_splunk_operator import instance_delete

def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'splunk.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_create.validate(task['operator'])
        if error is not None:
            return None, error

    if 'instance' in task:
        if not isinstance(task['instance'], list):
            return None, 'splunk.instance list required'

        for item in task['instance']:
            if not isinstance(item, dict):
                return None, 'splunk.instance list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item, error = instance_create.validate(item)
            if error is not None:
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
        return None, 'No valid parameters defined for splunk task'
    
    return new_task, None


def run(params, log_id=None):
    if 'operator' in params:
        success = operator_create.run(params['operator'], log_id=log_id)
        if not success:
            return False

    if 'instance' in params:
        for item in params['instance']:
            success = instance_create.run(item, log_id=log_id)
            if not success:
                return False
            
    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'splunk.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator'], error = operator_delete.validate(task['operator'])
        if error is not None:
            return None, error

    if 'instance' in task:
        if not isinstance(task['instance'], list):
            return None, 'splunk.instance list required'

        for item in task['instance']:
            if not isinstance(item, dict):
                return None, 'splunk.instance list of dict required'

            item['cluster'] = cluster_name
            item['instance'] = [item['instance']]
            item, error = instance_delete.validate(item)
            if error is not None:
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
        return None, 'No valid parameters defined for splunk task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'instance' in params:
        for item in params['instance']:
            success = instance_delete.run(item, log_id=log_id)
            if not success:
                return False
            
    if 'operator' in params:
        success = operator_delete.run(params['operator'], log_id=log_id)
        if not success:
            return False

    return True