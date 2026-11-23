import time
from lib import filter_helper


class K8sStorageClassLso():
    def __init__(self):
        pass

    def get_storage_class_name_local_storage(self, cache_enabled=True):
        info = self.get_storage_class_local_storage(cache_enabled=cache_enabled)
        if info is None:
            return None
        return info['name']
    
    def get_storage_class_local_storage(self, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'lso:true'
        )

        storage_classes = self.get_storage_classes(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )

        if storage_classes is None:
            return None

        if len(storage_classes) == 1:
            return storage_classes[0]

        return None
    