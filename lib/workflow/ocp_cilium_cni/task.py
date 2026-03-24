from lib.workflow.ocp_cilium_cni import image


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'set' in task:
        if not isinstance(task['set'], dict):
            return None, 'cilium_image.set dict required'

        task['set']['cluster'] = cluster_name
        task['set']['confirmation'] = confirmation
        task['set'], error = image.validate(task['set'])
        if error is not None:
            return None, error

    new_task = {}
    allowed_keys = [
        'set'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for cilium_image task'
    
    return new_task, None


def run(params, log_id=None):
    if 'set' in params:
        success = image.run(params['set'], log_id=log_id)
        if not success:
            return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    new_task = {}    
    return new_task, None


def delete(params, log_id=None):
    return True
