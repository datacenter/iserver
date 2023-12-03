from lib import filter_helper


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
