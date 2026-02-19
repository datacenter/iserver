from lib.workflow.ocp_cli import apply


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if not isinstance(task['location'], list):
        return None, 'cli.file.location list required'

    task['cluster'] = cluster_name
    task['confirmation'] = confirmation
    task, error = apply.validate(task)
    if error is not None:
        return None, error
    
    return task, None


def run(params, log_id=None):
    success = apply.run(params, log_id=log_id)
    if not success:
        return False

    return True
