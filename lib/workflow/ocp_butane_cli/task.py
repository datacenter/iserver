from lib.workflow.ocp_butane_cli import install


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation

    if not task['enabled']:
        return task, None

    return task, None

def run(params, log_id=None):
    if params['enabled']:
        return install.run(params, log_id=log_id)
    
    return True