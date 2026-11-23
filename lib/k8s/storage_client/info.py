from lib import filter_helper


class K8sStorageClientInfo():
    def __init__(self):
        self.storage_client = None

    def get_storage_client_info(self, storage_client_mo):
        if storage_client_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            storage_client_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(storage_client_mo, 'spec')
        info['status'] = self.get(storage_client_mo, 'status')
        return info

    def get_storage_clients_info(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_client is not None:
                return self.storage_client

        managed_objects = self.get_storage_client_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.storage_client = []
        for managed_object in managed_objects:
            storage_client_info = {}
            storage_client_info['info'] = self.get_storage_client_info(
                managed_object
            )
            storage_client_info['mo'] = managed_object
            self.storage_client.append(
                storage_client_info
            )

        return self.storage_client

    def match_storage_client(self, storage_client_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, storage_client_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_storage_client',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_storage_clients(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_storage_clients = self.get_storage_clients_info(cache_enabled=cache_enabled)
        if all_storage_clients is None:
            return None

        storage_clients = []

        for storage_client_info in all_storage_clients:
            if not self.match_storage_client(storage_client_info['info'], object_filter):
                continue

            if return_mo:
                storage_clients.append(
                    storage_client_info['mo']
                )
                continue

            storage_clients.append(
                storage_client_info['info']
            )

        return storage_clients

    def is_storage_client(self, name, cache_enabled=True):
        if self.get_storage_client(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_storage_client(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        storage_clients = self.get_storage_clients(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if storage_clients is None:
            return None

        if len(storage_clients) == 1:
            return storage_clients[0]

        return None
