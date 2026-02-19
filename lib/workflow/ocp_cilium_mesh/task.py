from lib.workflow.ocp_cilium_mesh import feature_enable
from lib.workflow.ocp_cilium_mesh import cluster_create
from lib.workflow.ocp_cilium_mesh import timescape_enable
from lib.workflow.ocp_cilium_mesh import feature_disable
from lib.workflow.ocp_cilium_mesh import cluster_delete
from lib.workflow.ocp_cilium_mesh import timescape_disable


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'feature' in task:
        if not isinstance(task['feature'], dict):
            return None, 'cilium_mesh.feature dict required'

        task['feature']['cluster'] = cluster_name
        task['feature']['confirmation'] = confirmation
        task['feature'], error = feature_enable.validate(task['feature'])
        if error is not None:
            return None, error
        
    if 'cluster' in task:
        if not isinstance(task['cluster'], list):
            return None, 'cilium_mesh.cluster list required'

        for item in task['cluster']:
            if not isinstance(item, dict):
                return None, 'cilium_mesh.cluster list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item, error = cluster_create.validate(item)
            if error is not None:
                return None, error

    if 'timescape' in task:
        if not isinstance(task['timescape'], dict):
            return None, 'cilium_mesh.timescape dict required'

        task['timescape']['cluster'] = cluster_name
        task['timescape']['confirmation'] = confirmation
        task['timescape'], error = timescape_enable.validate(task['timescape'])
        if error is not None:
            return None, error
                                
    new_task = {}
    allowed_keys = [
        'feature',
        'cluster',
        'timescape'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for cilium_mesh task'
    
    return new_task, None


def run(params, log_id=None):
    if 'feature' in params:
        success = feature_enable.run(params['feature'], log_id=log_id)
        if not success:
            return False

    if 'cluster' in params:
        for item in params['cluster']:
            success = cluster_create.run(item, log_id=log_id)
            if not success:
                return False

    if 'timescape' in params:
        success = timescape_enable.run(params['timescape'], log_id=log_id)
        if not success:
            return False
        
    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'feature' in task:
        if not isinstance(task['feature'], dict):
            return None, 'cilium_mesh.feature dict required'

        task['feature']['cluster'] = cluster_name
        task['feature']['confirmation'] = confirmation
        task['feature'], error = feature_disable.validate(task['feature'])
        if error is not None:
            return None, error

    if 'cluster' in task:
        if not isinstance(task['cluster'], list):
            return None, 'cilium_mesh.cluster list required'

        for item in task['cluster']:
            if not isinstance(item, dict):
                return None, 'cilium_mesh.cluster list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item, error = cluster_delete.validate(item)
            if error is not None:
                return None, error

    if 'timescape' in task:
        if not isinstance(task['timescape'], dict):
            return None, 'cilium_mesh.timescape dict required'

        task['timescape']['cluster'] = cluster_name
        task['timescape']['confirmation'] = confirmation
        task['timescape'], error = timescape_disable.validate(task['timescape'])
        if error is not None:
            return None, error
        
    new_task = {}
    allowed_keys = [
        'feature',
        'cluster',
        'timescape'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for cilium_mesh task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'cluster' in params:
        for item in params['cluster']:
            success = cluster_delete.run(item, log_id=log_id)
            if not success:
                return False

    if 'feature' in params:
        success = feature_disable.run(params['feature'], log_id=log_id)
        if not success:
            return False

    if 'timescape' in params:
        success = timescape_disable.run(params['timescape'], log_id=log_id)
        if not success:
            return False
            
    return True