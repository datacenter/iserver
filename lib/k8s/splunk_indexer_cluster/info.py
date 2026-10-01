class K8sSplunkIndexerClusterInfo():
    def __init__(self):
        self.splunk_indexer_cluster = None

    def get_splunk_indexer_cluster_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_splunk_indexer_clusters(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'splunk_indexer_cluster', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_splunk_indexer_cluster(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'splunk_indexer_cluster', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_splunk_indexer_cluster(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_splunk_indexer_cluster(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_splunk_indexer_cluster(self, cache_enabled=True):
        infos = self.get_splunk_indexer_clusters(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True