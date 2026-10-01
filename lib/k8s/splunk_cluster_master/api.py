class K8sSplunkClusterMasterApi():
    def __init__(self):
        self.splunk_cluster_master_mo = None
        self.splunk_cluster_master_namespace_mo = {}

    def get_splunk_cluster_master_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.splunk_cluster_master_mo,
            self.splunk_cluster_master_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.splunk_cluster_master_mo, self.splunk_cluster_master_namespace_mo = self.get_namespaced_resources(
            'ClusterMaster', 
            'enterprise.splunk.com/v3', 
            self.splunk_cluster_master_mo,
            self.splunk_cluster_master_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response