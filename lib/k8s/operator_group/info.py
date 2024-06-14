from lib import filter_helper


class K8sOperatorGroupInfo():
    def __init__(self):
        self.operator_group = None

    def get_operator_group_info(self, operator_group_mo):
        if operator_group_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            operator_group_mo
        )
        info.update(metadata_info)

        actual_namespaces = self.get(operator_group_mo, 'status:namespaces', on_error=[], on_none=[])
        info['ns'] = []
        for namespace_name in actual_namespaces:
            if len(namespace_name) == 0:
                continue

            ns_info = {}
            ns_info['__Output'] = {}
            ns_info['name'] = namespace_name
            info['ns'].append(
                ns_info
            )

        info['ns'] = sorted(
            info['ns'],
            key=lambda i: i['name']
        )
        info['nsCount'] = len(info['ns'])

        return info

    def get_operator_groups_info(self, cache_enabled=True):
        if cache_enabled:
            if self.operator_group is not None:
                return self.operator_group

        managed_objects = self.get_operator_group_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.operator_group = []
        for managed_object in managed_objects:
            operator_group_info = {}
            operator_group_info['info'] = self.get_operator_group_info(
                managed_object
            )
            operator_group_info['mo'] = managed_object
            self.operator_group.append(
                operator_group_info
            )

        return self.operator_group

    def match_operator_group(self, operator_group_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, operator_group_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (operator_group_info['namespace'], operator_group_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_operator_group',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_operator_groups(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_operator_groups = self.get_operator_groups_info(cache_enabled=cache_enabled)
        if all_operator_groups is None:
            return None

        operator_groups = []

        for operator_group_info in all_operator_groups:
            if not self.match_operator_group(operator_group_info['info'], object_filter):
                continue

            if return_mo:
                operator_groups.append(
                    operator_group_info['mo']
                )
                continue

            operator_groups.append(
                operator_group_info['info']
            )

        return operator_groups

    def is_operator_group(self, namespace, name, cache_enabled=True):
        if self.get_operator_group(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_operator_group(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        operator_groups = self.get_operator_groups(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if operator_groups is None:
            return None

        if len(operator_groups) == 1:
            return operator_groups[0]

        return None
