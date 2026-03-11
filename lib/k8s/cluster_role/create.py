from lib import ip_helper


class K8sClusterRoleCreate():
    def __init__(self):
        pass

    def get_cluster_role_create_body(self, name, api_groups=[], resources=[], verbs=[]):
        body = {}
        body['apiVersion'] = 'rbac.authorization.k8s.io/v1'
        body['kind'] = 'ClusterRole'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['rules'] = []

        rule_mo = {}
        if len(api_groups) > 0:
            rule_mo['apiGroups'] = api_groups

        if len(resources) > 0:
            rule_mo['resources'] = resources

        if len(verbs) > 0:
            rule_mo['verbs'] = verbs

        body['rules'].append(rule_mo)
        return body
    
    def create_cluster_role(
            self, 
            name, 
            api_groups=[], 
            resources=[], 
            verbs=[],
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_cluster_role(name, cache_enabled=False):
            name = '%s-%s' % (name, ip_helper.get_short_uuid())

        body = self.get_cluster_role_create_body(
            name, 
            api_groups=api_groups,
            resources=resources,
            verbs=verbs
        )
            
        if not self.create_resource(body, object_name='cluster_role', my_output=my_output, confirmation=confirmation):
            return None

        if not wait:
            return name

        success = self.wait_cluster_role(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return None
        
        return name
    
    def create_or_update_cluster_role(
            self, 
            name, 
            api_groups=[], 
            resources=[], 
            verbs=[],
            replace=True,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_cluster_role(name, cache_enabled=False):
            return self.update_cluster_role(
                name,
                api_groups=api_groups, 
                resources=resources, 
                verbs=verbs,
                replace=replace,
                confirmation=confirmation, 
                my_output=my_output
            )

        return self.create_cluster_role(
            name,
            api_groups=api_groups, 
            resources=resources, 
            verbs=verbs,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )
    
    def get_service_account_cluster_role_body(self, name, cluster_role_name, sa_name, sa_namespace):
        body = {}
        body['apiVersion'] = 'rbac.authorization.k8s.io/v1'
        body['kind'] = 'ClusterRole'
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
    
    def add_service_account_cluster_role(
            self, 
            name, 
            cluster_role_name, 
            sa_name, 
            sa_namespace,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_cluster_role(name, cache_enabled=False):
            name = '%s-%s' % (name, ip_helper.get_short_uuid())

        body = self.get_service_account_cluster_role_body(name, cluster_role_name, sa_name, sa_namespace)
        if not self.create_resource(body, object_name='cluster_role', my_output=my_output, confirmation=confirmation):
            return None

        if not wait:
            return name

        success = self.wait_cluster_role(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return None
        
        return name