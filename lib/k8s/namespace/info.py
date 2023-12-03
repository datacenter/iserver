from lib import filter_helper


class K8sNamespaceInfo():
    def __init__(self):
        self.namespace = None

    def get_namespace_info(self, namespace_mo):
        if namespace_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            namespace_mo
        )
        info.update(metadata_info)

        info['phase'] = self.get(namespace_mo, 'status:phase')
        if info['phase'] is not None and info['phase'] == 'Active':
            info['__Output']['phase'] = 'Green'
        else:
            info['__Output']['phase'] = 'Red'

        return info

    def get_namespaces_info(self, cache_enabled=True):
        if cache_enabled:
            if self.namespace is not None:
                return self.namespace

        managed_objects = self.get_namespace_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.namespace = []
        for managed_object in managed_objects:
            namespace_info = {}
            namespace_info['info'] = self.get_namespace_info(
                managed_object
            )
            namespace_info['mo'] = managed_object
            self.namespace.append(
                namespace_info
            )

        return self.namespace

    def match_namespace(self, namespace_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, namespace_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_namespace',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_namespaces(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_namespaces = self.get_namespaces_info(cache_enabled=cache_enabled)
        if all_namespaces is None:
            return None

        namespaces = []

        for namespace_info in all_namespaces:
            if not self.match_namespace(namespace_info['info'], object_filter):
                continue

            if return_mo:
                namespaces.append(
                    namespace_info['mo']
                )
                continue

            namespaces.append(
                namespace_info['info']
            )

        return namespaces

    def is_namespace(self, name, cache_enabled=True):
        if self.get_namespace(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_namespace(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        namespaces = self.get_namespaces(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if namespaces is None:
            return None

        if len(namespaces) == 1:
            return namespaces[0]

        return None
