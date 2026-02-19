from lib.workflow.ocp_imm import configure as imm_create
from lib.workflow.ocp_imm import unconfigure as imm_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation
    task, error = imm_create.validate(task)
    return task, error


def run(params, log_id=None):
    return imm_create.run(params, log_id=log_id)


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation
    task, error = imm_delete.validate(task)
    return task, error


def delete(params, log_id=None):
    return imm_delete.run(params, log_id=log_id)
