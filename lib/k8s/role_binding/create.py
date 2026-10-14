import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sRoleBindingCreate():
    def __init__(self):
        pass

    def create_service_account_role_binding(self, namespace, name, cluster_role_name, sa_namespace, sa_name, my_output=None, confirmation=False):
        if my_output is not None:
            my_output.default('Create role binding', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- cluster role: %s' % (cluster_role_name))
            my_output.default('- service account namespace: %s' % (sa_namespace))
            my_output.default('- service account name: %s' % (sa_name))
            
        if my_output is None:
            confirmation = False
        
        if self.is_role_binding(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already created')
            return True
        
        body = {}
        body['apiVersion'] = 'rbac.authorization.k8s.io/v1'
        body['kind'] = 'RoleBinding'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
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

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False
            
        success, _ = self.create_resource(body)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False

        if my_output is not None:
            my_output.default('Role binding created', before_newline=True)

        return True

    def create_or_update_service_account_role_binding(self, namespace, name, cluster_role_name, sa_namespace, sa_name, my_output=None, confirmation=False):
        rb = self.get_role_binding(namespace, name, cache_enabled=False)
        if rb is None:
            return self.create_service_account_role_binding(
                namespace, 
                name, 
                cluster_role_name, 
                sa_namespace, 
                sa_name, 
                my_output=my_output, 
                confirmation=confirmation
            )

        if rb['role']['name'] != cluster_role_name:
            if my_output is not None:
                my_output.error(
                    'Request inconsistent with role binding %s/%s. Different roleRef. Actual %s vs expected %s' % (
                        namespace,
                        name,
                        rb['role']['name'],
                        cluster_role_name
                    )
                )
            return False

        for subnet in rb['subject']:
            if subnet['kind'] != 'ServiceAccount':
                continue

            if subnet['namespace'] != sa_namespace:
                continue

            if subnet['name'] != sa_name:
                continue

            if my_output is not None:
                my_output.default(
                    'Role binding %s/%s is already configured with ServiceAccount %s/%s for role %s' % (
                        namespace,
                        name,
                        sa_namespace,
                        sa_name,
                        cluster_role_name
                    )
                )

            return True

        body = {}
        body['apiVersion'] = 'rbac.authorization.k8s.io/v1'
        body['kind'] = 'RoleBinding'
        body['metadata'] = {}
        body['metadata']['namespace'] = rb['namespace']
        body['metadata']['name'] = rb['name']
        body['metadata']['resource_version'] = rb['resource_version']
        body['roleRef'] = rb['role']
        body['subjects'] = rb['subject']

        for item in body['subjects']:
            if 'description' in item:
                del item['description']

        new_subject = {}
        new_subject['kind'] = 'ServiceAccount'
        new_subject['namespace'] = sa_namespace
        new_subject['name'] = sa_name
        body['subjects'].append(new_subject)

        return self.replace_resource(body, object_name='role_binding', my_output=my_output, confirmation=confirmation)