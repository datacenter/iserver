from lib.workflow.ocp_intersight_operator import operator_create
from lib.workflow.ocp_intersight_operator import instance_create
from lib.workflow.ocp_intersight_operator import enable_plugin
from lib.workflow.ocp_intersight_operator import register
from lib.workflow.ocp_intersight_operator import operator_delete
from lib.workflow.ocp_intersight_operator import instance_delete
from lib.workflow.ocp_intersight_operator import disable_plugin


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'intersight.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator']['base_directory'] = cluster_settings['directory']
        task['operator'], error = operator_create.validate(task['operator'])
        if error is not None:
            return None, error
    
    if 'instance' in task:
        if not isinstance(task['instance'], dict):
            return None, 'intersight.instance dict required'

        task['instance']['cluster'] = cluster_name
        task['instance']['confirmation'] = confirmation
        task['instance']['base_directory'] = cluster_settings['directory']
        task['instance'], error = instance_create.validate(task['instance'])
        if error is not None:
            return None, error

    if 'ui' in task:
        if not isinstance(task['ui'], dict):
            return None, 'intersight.ui dict required'

        task['ui']['cluster'] = cluster_name
        task['ui']['confirmation'] = confirmation
        task['ui']['base_directory'] = cluster_settings['directory']
        task['ui'], error = enable_plugin.validate(task['ui'])
        if error is not None:
            return None, error

    if 'register' in task:
        if not isinstance(task['register'], dict):
            return None, 'intersight.register dict required'

        task['register']['cluster'] = cluster_name
        task['register']['confirmation'] = confirmation
        task['register']['base_directory'] = cluster_settings['directory']
        task['register'], error = register.validate(task['register'])
        if error is not None:
            return None, error
                
    new_task = {}
    allowed_keys = [
        'operator',
        'instance',
        'ui',
        'register'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for intersight task'
    
    return new_task, None


def run(params, log_id=None):
    if 'operator' in params:
        success = operator_create.run(params['operator'], log_id=log_id)
        if not success:
            return False

    if 'instance' in params:
        success = instance_create.run(params['instance'], log_id=log_id)
        if not success:
            return False
        
    if 'ui' in params:
        success = enable_plugin.run(params['ui'], log_id=log_id)
        if not success:
            return False

    if 'register' in params:
        success = register.run(params['register'], log_id=log_id)
        if not success:
            return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'intersight.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_delete.validate(task['operator'])
        if error is not None:
            return None, error
    
    if 'instance' in task:
        if not isinstance(task['instance'], dict):
            return None, 'intersight.instance dict required'

        task['instance']['cluster'] = cluster_name
        task['instance']['confirmation'] = confirmation
        task['instance'], error = instance_delete.validate(task['instance'])
        if error is not None:
            return None, error

    if 'ui' in task:
        if not isinstance(task['ui'], dict):
            return None, 'intersight.ui dict required'

        task['ui']['cluster'] = cluster_name
        task['ui']['confirmation'] = confirmation
        task['ui'], error = disable_plugin.validate(task['ui'])
        if error is not None:
            return None, error

    new_task = {}
    allowed_keys = [
        'operator',
        'instance',
        'ui'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for intersight task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'ui' in params:
        success = disable_plugin.run(params['ui'], log_id=log_id)
        if not success:
            return False
        
    if 'instance' in params:
        success = instance_delete.run(params['instance'], log_id=log_id)
        if not success:
            return False
        
    if 'operator' in params:
        success = operator_delete.run(params['operator'], log_id=log_id)
        if not success:
            return False

    return True