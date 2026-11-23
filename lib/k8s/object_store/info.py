from lib import filter_helper


class K8sObjectStoreInfo():
    def __init__(self):
        self.object_store = None

    def get_object_store_info(self, managed_object):
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

    def get_object_stores_info(self, cache_enabled=True):
        if cache_enabled:
            if self.object_store is not None:
                return self.object_store

        managed_objects = self.get_object_store_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.object_store = []
        for managed_object in managed_objects:
            object_store_info = {}
            object_store_info['info'] = self.get_object_store_info(
                managed_object
            )
            object_store_info['mo'] = managed_object
            self.object_store.append(
                object_store_info
            )

        return self.object_store

    def match_object_store(self, object_store_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, object_store_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, object_store_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_object_store',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_object_stores(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_object_stores = self.get_object_stores_info(cache_enabled=cache_enabled)
        if all_object_stores is None:
            return None

        object_stores = []

        for object_store_info in all_object_stores:
            if not self.match_object_store(object_store_info['info'], object_filter):
                continue

            if return_mo:
                object_stores.append(
                    object_store_info['mo']
                )
                continue

            object_stores.append(
                object_store_info['info']
            )

        return object_stores

    def is_object_store(self, namespace, name, cache_enabled=True):
        if self.get_object_store(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_object_store(self, cache_enabled=True):
        policies = self.get_object_stores(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_object_store(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        object_stores = self.get_object_stores(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if object_stores is None:
            return None

        if len(object_stores) == 1:
            return object_stores[0]

        return None
