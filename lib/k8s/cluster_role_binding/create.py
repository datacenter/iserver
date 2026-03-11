from lib import ip_helper


class K8sClusterRoleBindingCreate():
    def __init__(self):
        pass

    def get_create_cluster_role_binding_service_account_body(
            self,
            name,
            cluster_role_name, 
            sa_namespace,
            sa_name
        ):
        body = {}
        body['apiVersion'] = 'rbac.authorization.k8s.io/v1'
        body['kind'] = 'ClusterRoleBinding'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['roleRef'] = {}
        body['roleRef']['apiGroup'] = 'rbac.authorization.k8s.io'
        body['roleRef']['kind'] = 'ClusterRole'
        body['roleRef']['name'] = cluster_role_name
        body['subjects'] = []

        subject = {}
        subject['kind'] = 'ServiceAccount'
        subject['name'] = sa_name
        subject['namespace'] = sa_namespace
        body['subjects'].append(
            subject
        )
        return body

    def create_service_account_cluster_role_binding(
            self, 
            name, 
            cluster_role_name, 
            sa_name, 
            sa_namespace,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_cluster_role_binding(name, cache_enabled=False):
            name = '%s-%s' % (name, ip_helper.get_short_uuid())

        body = self.get_create_cluster_role_binding_service_account_body(
            name,
            cluster_role_name, 
            sa_namespace,
            sa_name
        )
        if not self.create_resource(body, object_name='cluster_role_binding', my_output=my_output, confirmation=confirmation):
            return None

        if not wait:
            return name

        success = self.wait_cluster_role_binding(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return None
        
        return name

    def create_or_update_service_account_cluster_role_binding(
            self, 
            name, 
            cluster_role_name, 
            sa_name, 
            sa_namespace,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_cluster_role_binding(name, cache_enabled=False):
            return self.update_service_account_cluster_role_binding(
                name, 
                cluster_role_name, 
                sa_name, 
                sa_namespace,
                confirmation=confirmation, 
                my_output=my_output      
            )
        
        name = self.create_service_account_cluster_role_binding(
            name, 
            cluster_role_name, 
            sa_name, 
            sa_namespace,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )
        if name is None:
            return False
        
        return True
    