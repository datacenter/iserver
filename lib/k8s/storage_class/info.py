from lib import filter_helper


class K8sStorageClassInfo():
    def __init__(self):
        self.storage_class = None

    def get_storage_class_info(self, storage_class_mo):
        if storage_class_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            storage_class_mo
        )
        info.update(metadata_info)

        return info

    def get_storage_classes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_class is not None:
                return self.storage_class

        managed_objects = self.get_storage_class_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.storage_class = []
        for managed_object in managed_objects:
            storage_class_info = {}
            storage_class_info['info'] = self.get_storage_class_info(
                managed_object
            )
            storage_class_info['mo'] = managed_object
            self.storage_class.append(
                storage_class_info
            )

        return self.storage_class

    def match_storage_class(self, storage_class_info, storage_class_filter):
        if storage_class_filter is None or len(storage_class_filter) == 0:
            return True

        for ap_rule in storage_class_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_storage_class',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_storage_classes(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_storage_classes = self.get_storage_classes_info(cache_enabled=cache_enabled)
        if all_storage_classes is None:
            return None

        storage_classes = []

        for storage_class_info in all_storage_classes:
            if not self.match_storage_class(storage_class_info['info'], object_filter):
                continue

            if return_mo:
                storage_classes.append(
                    storage_class_info['mo']
                )
                continue

            storage_classes.append(
                storage_class_info['info']
            )

        return storage_classes
