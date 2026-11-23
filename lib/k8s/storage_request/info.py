from lib import filter_helper


class K8sStorageRequestInfo():
    def __init__(self):
        self.storage_request = None

    def get_storage_request_info(self, storage_request_mo):
        if storage_request_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            storage_request_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(storage_request_mo, 'spec')
        info['status'] = self.get(storage_request_mo, 'status')
        return info

    def get_storage_requests_info(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_request is not None:
                return self.storage_request

        managed_objects = self.get_storage_request_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.storage_request = []
        for managed_object in managed_objects:
            storage_request_info = {}
            storage_request_info['info'] = self.get_storage_request_info(
                managed_object
            )
            storage_request_info['mo'] = managed_object
            self.storage_request.append(
                storage_request_info
            )

        return self.storage_request

    def match_storage_request(self, storage_request_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, storage_request_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, storage_request_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_storage_request',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_storage_requests(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_storage_requests = self.get_storage_requests_info(cache_enabled=cache_enabled)
        if all_storage_requests is None:
            return None

        storage_requests = []

        for storage_request_info in all_storage_requests:
            if not self.match_storage_request(storage_request_info['info'], object_filter):
                continue

            if return_mo:
                storage_requests.append(
                    storage_request_info['mo']
                )
                continue

            storage_requests.append(
                storage_request_info['info']
            )

        return storage_requests

    def is_storage_request(self, namespace, name, cache_enabled=True):
        if self.get_storage_request(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_storage_request(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        storage_requests = self.get_storage_requests(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if storage_requests is None:
            return None

        if len(storage_requests) == 1:
            return storage_requests[0]

        return None
