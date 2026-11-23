from lib import filter_helper


class K8sPolicyBindingInfo():
    def __init__(self):
        self.policy_binding = None

    def get_policy_binding_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')
        return info

    def get_policy_bindings_info(self, cache_enabled=True):
        if cache_enabled:
            if self.policy_binding is not None:
                return self.policy_binding

        managed_objects = self.get_policy_binding_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.policy_binding = []
        for managed_object in managed_objects:
            policy_binding_info = {}
            policy_binding_info['info'] = self.get_policy_binding_info(
                managed_object
            )
            policy_binding_info['mo'] = managed_object
            self.policy_binding.append(
                policy_binding_info
            )

        return self.policy_binding

    def match_policy_binding(self, policy_binding_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, policy_binding_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, policy_binding_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_policy_binding',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_policy_bindings(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_policy_bindings = self.get_policy_bindings_info(cache_enabled=cache_enabled)
        if all_policy_bindings is None:
            return None

        policy_bindings = []

        for policy_binding_info in all_policy_bindings:
            if not self.match_policy_binding(policy_binding_info['info'], object_filter):
                continue

            if return_mo:
                policy_bindings.append(
                    policy_binding_info['mo']
                )
                continue

            policy_bindings.append(
                policy_binding_info['info']
            )

        return policy_bindings

    def is_policy_binding(self, namespace, name, cache_enabled=True):
        if self.get_policy_binding(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_policy_binding(self, cache_enabled=True):
        policies = self.get_policy_bindings(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_policy_binding(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        policy_bindings = self.get_policy_bindings(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if policy_bindings is None:
            return None

        if len(policy_bindings) == 1:
            return policy_bindings[0]

        return None
