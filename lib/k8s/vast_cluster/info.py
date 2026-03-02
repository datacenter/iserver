class K8sVastClusterInfo():
    def __init__(self):
        self.vast_cluster = None

    def get_vast_cluster_info(self, managed_object):
        return self.get_vast_managed_object_info(managed_object)

    def get_vast_clusters(self, object_filter=None, storage_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'vast_cluster', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

        if return_mo:
            return infos
        
        if storage_info:
            for item in infos:
                item['storage'] = []

            storages = self.get_vast_storages(cache_enabled=cache_enabled)
            if storages is not None:
                for storage in storages:
                    for item in infos:
                        if self.get(storage, 'spec:secretName') == item['name']:
                            item['storage'].append(storage['name'])

        return infos

    def is_vast_cluster(self, namespace, name, cache_enabled=True):
        if self.get_vast_cluster(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_vast_cluster(self, namespace, name, storage_info=False, return_mo=False, cache_enabled=True):
        return self.get_info(
            'vast_cluster', 
            name,
            namespace=namespace,
            storage_info=storage_info,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
    