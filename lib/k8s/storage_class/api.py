class K8sStorageClassApi():
    def __init__(self):
        self.storage_class_mo = None

    def get_storage_class_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.storage_class_mo
        )
        if cache_hit:
            return response

        response, self.storage_class_mo = self.get_resources(
            'StorageClass', 
            'storage.k8s.io/v1', 
            self.storage_class_mo,
            name=name
        )

        return response

    def delete_storage_class_mo(self, name):
        success, _ = self.delete_resource('StorageClass', 'storage.k8s.io/v1', name)
        return success