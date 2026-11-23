from lib import filter_helper


class K8sObjectTransferInfo():
    def __init__(self):
        self.object_transfer = None

    def get_object_transfer_info(self, object_transfer_mo):
        if object_transfer_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            object_transfer_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(object_transfer_mo, 'spec')
        info['status'] = self.get(object_transfer_mo, 'status')
        return info

    def get_object_transfers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.object_transfer is not None:
                return self.object_transfer

        managed_objects = self.get_object_transfer_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.object_transfer = []
        for managed_object in managed_objects:
            object_transfer_info = {}
            object_transfer_info['info'] = self.get_object_transfer_info(
                managed_object
            )
            object_transfer_info['mo'] = managed_object
            self.object_transfer.append(
                object_transfer_info
            )

        return self.object_transfer

    def match_object_transfer(self, object_transfer_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, object_transfer_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_object_transfer',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_object_transfers(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_object_transfers = self.get_object_transfers_info(cache_enabled=cache_enabled)
        if all_object_transfers is None:
            return None

        object_transfers = []

        for object_transfer_info in all_object_transfers:
            if not self.match_object_transfer(object_transfer_info['info'], object_filter):
                continue

            if return_mo:
                object_transfers.append(
                    object_transfer_info['mo']
                )
                continue

            object_transfers.append(
                object_transfer_info['info']
            )

        return object_transfers

    def is_object_transfer(self, name, cache_enabled=True):
        if self.get_object_transfer(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_object_transfer(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        object_transfers = self.get_object_transfers(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if object_transfers is None:
            return None

        if len(object_transfers) == 1:
            return object_transfers[0]

        return None
