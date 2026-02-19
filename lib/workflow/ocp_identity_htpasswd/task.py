from lib.workflow.ocp_identity_htpasswd import add as htpasswd_create
from lib.workflow.ocp_identity_htpasswd import delete as htpasswd_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['base_directory'] = cluster_settings['directory']
    task['confirmation'] = confirmation
    task, error = htpasswd_create.validate(task)
    return task, error


def run(params, log_id=None):
    return htpasswd_create.run(params, log_id=log_id)


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['base_directory'] = cluster_settings['directory']
    task['confirmation'] = confirmation
    task, error = htpasswd_delete.validate(task)
    return task, error


def delete(params, log_id=None):
    return htpasswd_delete.run(params, log_id=log_id)
