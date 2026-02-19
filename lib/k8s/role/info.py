from lib import filter_helper


class K8sRoleInfo():
    def __init__(self):
        self.role = None

    def get_role_info(self, role_mo):
        if role_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            role_mo
        )
        info.update(metadata_info)

        info['role'] = self.get(role_mo, 'roleRef')
        info['subject'] = self.get(role_mo, 'subjects', on_error=[], on_none=[])
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

    def get_roles_info(self, cache_enabled=True):
        if cache_enabled:
            if self.role is not None:
                return self.role

        managed_objects = self.get_role_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.role = []
        for managed_object in managed_objects:
            role_info = {}
            role_info['info'] = self.get_role_info(
                managed_object
            )
            role_info['mo'] = managed_object
            self.role.append(
                role_info
            )

        return self.role

    def match_role(self, role_info, role_filter):
        if role_filter is None or len(role_filter) == 0:
            return True

        for ap_rule in role_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, role_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (role_info['namespace'], role_info['name'])):
                    return False

            if key == 'subject':
                key_found = True
                found = False
                for subject in role_info['subject']:
                    if filter_helper.match_string(value, subject['description']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_role',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_roles(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_roles = self.get_roles_info(cache_enabled=cache_enabled)
        if all_roles is None:
            return None

        roles = []

        for role_info in all_roles:
            if not self.match_role(role_info['info'], object_filter):
                continue

            if return_mo:
                roles.append(
                    role_info['mo']
                )
                continue

            roles.append(
                role_info['info']
            )

        return roles

    def is_role(self, namespace, name, cache_enabled=True):
        if self.get_role(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True
    
    def get_role(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        roles = self.get_roles(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if roles is None:
            return None

        if len(roles) == 1:
            return roles[0]

        return None
