from lib import filter_helper


class K8sStorageConsumerInfo():
    def __init__(self):
        self.storage_consumer = None

    def get_storage_consumer_info(self, storage_consumer_mo):
        if storage_consumer_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            storage_consumer_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(storage_consumer_mo, 'spec')
        info['status'] = self.get(storage_consumer_mo, 'status')
        return info

    def get_storage_consumers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_consumer is not None:
                return self.storage_consumer

        managed_objects = self.get_storage_consumer_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.storage_consumer = []
        for managed_object in managed_objects:
            storage_consumer_info = {}
            storage_consumer_info['info'] = self.get_storage_consumer_info(
                managed_object
            )
            storage_consumer_info['mo'] = managed_object
            self.storage_consumer.append(
                storage_consumer_info
            )

        return self.storage_consumer

    def match_storage_consumer(self, storage_consumer_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, storage_consumer_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, storage_consumer_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_storage_consumer',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_storage_consumers(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_storage_consumers = self.get_storage_consumers_info(cache_enabled=cache_enabled)
        if all_storage_consumers is None:
            return None

        storage_consumers = []

        for storage_consumer_info in all_storage_consumers:
            if not self.match_storage_consumer(storage_consumer_info['info'], object_filter):
                continue

            if return_mo:
                storage_consumers.append(
                    storage_consumer_info['mo']
                )
                continue

            storage_consumers.append(
                storage_consumer_info['info']
            )

        return storage_consumers

    def is_storage_consumer(self, namespace, name, cache_enabled=True):
        if self.get_storage_consumer(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_storage_consumer(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        storage_consumers = self.get_storage_consumers(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if storage_consumers is None:
            return None

        if len(storage_consumers) == 1:
            return storage_consumers[0]

        return None
