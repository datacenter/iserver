from lib.workflow.ocp_nfs_helm import install


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation
    task, error = install.validate(task)
    return task, error
