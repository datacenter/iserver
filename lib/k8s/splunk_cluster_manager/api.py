class K8sSplunkClusterManagerApi():
    def __init__(self):
        self.splunk_cluster_manager_mo = None
        self.splunk_cluster_manager_namespace_mo = {}

    def get_splunk_cluster_manager_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.splunk_cluster_manager_mo,
            self.splunk_cluster_manager_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.splunk_cluster_manager_mo, self.splunk_cluster_manager_namespace_mo = self.get_namespaced_resources(
            'ClusterManager', 
            'enterprise.splunk.com/v4', 
            self.splunk_cluster_manager_mo,
            self.splunk_cluster_manager_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response