from lib.workflow.ocp_proxy import set


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation
    task, error = set.validate(task)
    if error is not None:
        return None, error

    return task, None


def run(params, log_id=None):
    success = set.run(params, log_id=log_id)
    if not success:
        return False
        
    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    return task, None


def delete(params, log_id=None):
    return True
