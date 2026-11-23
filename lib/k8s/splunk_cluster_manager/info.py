class K8sSplunkClusterManagerInfo():
    def __init__(self):
        self.splunk_cluster_manager = None

    def get_splunk_cluster_manager_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_splunk_cluster_managers(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'splunk_cluster_manager', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_splunk_cluster_manager(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'splunk_cluster_manager', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_splunk_cluster_manager(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_splunk_cluster_manager(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_splunk_cluster_manager(self, cache_enabled=True):
        infos = self.get_splunk_cluster_managers(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True