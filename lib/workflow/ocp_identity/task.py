from lib.workflow.ocp_identity_htpasswd import task as htpasswd
from lib.workflow.ocp_identity_ldap import task as ldap


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation

    if 'type' not in task:
        return None, 'identity task requires provider type'

    if task['type'] not in ['htpasswd', 'kubeadmin', 'ldap']:
        return None, 'identity task supported provider types: htpasswd, kubeadmin, ldap'

    if task['type'] == 'htpasswd':
        return htpasswd.validate_create(task, cluster_name, confirmation, cluster_settings=cluster_settings, k8s_handler=k8s_handler)
        
    if task['type'] == 'ldap':
        return ldap.validate_create(task, cluster_name, confirmation, cluster_settings=cluster_settings, k8s_handler=k8s_handler)
        
    if task['type'] == 'kubeadmin':
        if 'delete' not in task:
            task['delete'] = False

    return task, None

def run(params, log_id=None):
    if params['type'] == 'htpasswd':
        return htpasswd.run(params, log_id=log_id)
    
    if params['type'] == 'ldap':
        return ldap.run(params, log_id=log_id)
    
    return True

def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation

    if 'type' not in task:
        return None, 'identity task requires provider type'

    if task['type'] not in ['htpasswd', 'kubeadmin', 'ldap']:
        return None, 'identity task supported provider types: htpasswd, kubeadmin'

    if task['type'] == 'htpasswd':
        return htpasswd.validate_delete(task, cluster_name, confirmation, cluster_settings=cluster_settings, k8s_handler=k8s_handler)
        
    if task['type'] == 'ldap':
        return ldap.validate_delete(task, cluster_name, confirmation, cluster_settings=cluster_settings, k8s_handler=k8s_handler)
        
    if task['type'] == 'kubeadmin':
        if 'delete' not in task:
            task['delete'] = False

    return task, None

def delete(params, log_id=None):
    if params['type'] == 'htpasswd':
        return htpasswd.delete(params, log_id=log_id)
    
    if params['type'] == 'ldap':
        return ldap.delete(params, log_id=log_id)

    return True
