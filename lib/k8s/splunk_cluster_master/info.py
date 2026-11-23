class K8sSplunkClusterMasterInfo():
    def __init__(self):
        self.splunk_cluster_master = None

    def get_splunk_cluster_master_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_splunk_cluster_masters(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'splunk_cluster_master', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_splunk_cluster_master(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'splunk_cluster_master', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_splunk_cluster_master(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_splunk_cluster_master(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_splunk_cluster_master(self, cache_enabled=True):
        infos = self.get_splunk_cluster_masters(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True