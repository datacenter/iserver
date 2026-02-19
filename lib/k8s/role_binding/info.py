import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sRoleBindingInfo():
    def __init__(self):
        self.role_binding = None

    def get_role_binding_info(self, role_binding_mo):
        if role_binding_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            role_binding_mo
        )
        info.update(metadata_info)

        info['role'] = self.get(role_binding_mo, 'roleRef')
        info['subject'] = self.get(role_binding_mo, 'subjects', on_error=[], on_none=[])
        for subject in info['subject']:
            if 'namespace' in subject:
                subject['description'] = '%s:%s/%s' % (
                    subject['kind'],
                    subject['namespace'],
                    subject['name']
                )
            else:
                subject['description'] = '%s:%s' % (
                    subject['kind'],
                    subject['name']
                )

        return info

    def get_role_bindings_info(self, cache_enabled=True):
        if cache_enabled:
            if self.role_binding is not None:
                return self.role_binding

        managed_objects = self.get_role_binding_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.role_binding = []
        for managed_object in managed_objects:
            role_binding_info = {}
            role_binding_info['info'] = self.get_role_binding_info(
                managed_object
            )
            role_binding_info['mo'] = managed_object
            self.role_binding.append(
                role_binding_info
            )

        return self.role_binding

    def match_role_binding(self, role_binding_info, role_binding_filter):
        if role_binding_filter is None or len(role_binding_filter) == 0:
            return True

        for ap_rule in role_binding_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, role_binding_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (role_binding_info['namespace'], role_binding_info['name'])):
                    return False

            if key == 'subject':
                key_found = True
                found = False
                for subject in role_binding_info['subject']:
                    if filter_helper.match_string(value, subject['description']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_role_binding',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_role_bindings(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_role_bindings = self.get_role_bindings_info(cache_enabled=cache_enabled)
        if all_role_bindings is None:
            return None

        role_bindings = []

        for role_binding_info in all_role_bindings:
            if not self.match_role_binding(role_binding_info['info'], object_filter):
                continue

            if return_mo:
                role_bindings.append(
                    role_binding_info['mo']
                )
                continue

            role_bindings.append(
                role_binding_info['info']
            )

        return role_bindings

    def is_role_binding(self, namespace, name, cache_enabled=True):
        if self.get_role_binding(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True
    
    def get_role_binding(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        role_bindings = self.get_role_bindings(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if role_bindings is None:
            return None

        if len(role_bindings) == 1:
            return role_bindings[0]

        return None

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
            
        success = self.create_role_binding_mo(body)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False

        if my_output is not None:
            my_output.default('Role binding created', before_newline=True)

        return True
