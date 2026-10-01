class K8sSplunkSearchHeadClusterInfo():
    def __init__(self):
        self.splunk_search_head_cluster = None

    def get_splunk_search_head_cluster_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_splunk_search_head_clusters(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'splunk_search_head_cluster', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_splunk_search_head_cluster(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'splunk_search_head_cluster', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_splunk_search_head_cluster(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_splunk_search_head_cluster(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_splunk_search_head_cluster(self, cache_enabled=True):
        infos = self.get_splunk_search_head_clusters(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True