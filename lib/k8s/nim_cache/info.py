from lib import filter_helper


class K8sNimCacheInfo():
    def __init__(self):
        self.nim_cache = None

    def get_nim_cache_info(self, managed_object):
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

    def get_nim_caches_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nim_cache is not None:
                return self.nim_cache

        managed_objects = self.get_nim_cache_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nim_cache = []
        for managed_object in managed_objects:
            nim_cache_info = {}
            nim_cache_info['info'] = self.get_nim_cache_info(
                managed_object
            )
            nim_cache_info['mo'] = managed_object
            self.nim_cache.append(
                nim_cache_info
            )

        return self.nim_cache

    def match_nim_cache(self, nim_cache_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, nim_cache_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, nim_cache_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nim_cache',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nim_caches(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nim_caches = self.get_nim_caches_info(cache_enabled=cache_enabled)
        if all_nim_caches is None:
            return None

        nim_caches = []

        for nim_cache_info in all_nim_caches:
            if not self.match_nim_cache(nim_cache_info['info'], object_filter):
                continue

            if return_mo:
                nim_caches.append(
                    nim_cache_info['mo']
                )
                continue

            nim_caches.append(
                nim_cache_info['info']
            )

        return nim_caches

    def is_nim_cache(self, namespace, name, cache_enabled=True):
        if self.get_nim_cache(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_nim_cache(self, cache_enabled=True):
        policies = self.get_nim_caches(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_nim_cache(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        nim_caches = self.get_nim_caches(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nim_caches is None:
            return None

        if len(nim_caches) == 1:
            return nim_caches[0]

        return None
