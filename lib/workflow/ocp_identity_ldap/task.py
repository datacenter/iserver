from lib import filter_helper
from lib.workflow.ocp_identity_ldap import add as ldap_create
from lib.workflow.ocp_identity_ldap import delete as ldap_delete
from lib.workflow.ocp_identity_ldap import sync_add
from lib.workflow.ocp_identity_ldap import sync_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['base_directory'] = cluster_settings['directory']
    task['confirmation'] = confirmation
    if filter_helper.get(task, 'mode') == 'sync':
        task, error = sync_add.validate(task)
    else:
        task, error = ldap_create.validate(task)
    return task, error


def run(params, log_id=None):
    if filter_helper.get(params, 'mode') == 'sync':
        return sync_add.run(params, log_id=log_id)
    return ldap_create.run(params, log_id=log_id)


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['base_directory'] = cluster_settings['directory']
    task['confirmation'] = confirmation
    if filter_helper.get(task, 'mode') == 'sync':
        task, error = sync_delete.validate(task)
    else:
        task, error = ldap_delete.validate(task)
    return task, error


def delete(params, log_id=None):
    if filter_helper.get(params, 'mode') == 'sync':
        return sync_delete.run(params, log_id=log_id)
    return ldap_delete.run(params, log_id=log_id)
