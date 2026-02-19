from lib.workflow.ocp_ssh import create as ssh_create
from lib.workflow.ocp_ssh import delete as ssh_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['base_directory'] = cluster_settings['directory']
    task['filename'] = task['filename']
    task['confirmation'] = confirmation
    task, error = ssh_create.validate(task)
    return task, error


def run(params, log_id=None):
    return ssh_create.run(params, log_id=log_id)


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['base_directory'] = cluster_settings['directory']
    task['filename'] = task['filename']
    task['confirmation'] = confirmation
    task, error = ssh_delete.validate(task)
    return task, error


def delete(params, log_id=None):
    return ssh_delete.run(params, log_id=log_id)
