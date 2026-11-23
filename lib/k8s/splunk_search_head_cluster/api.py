class K8sSplunkSearchHeadClusterApi():
    def __init__(self):
        self.splunk_search_head_cluster_mo = None
        self.splunk_search_head_cluster_namespace_mo = {}

    def get_splunk_search_head_cluster_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.splunk_search_head_cluster_mo,
            self.splunk_search_head_cluster_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.splunk_search_head_cluster_mo, self.splunk_search_head_cluster_namespace_mo = self.get_namespaced_resources(
            'SearchHeadCluster', 
            'enterprise.splunk.com/v4', 
            self.splunk_search_head_cluster_mo,
            self.splunk_search_head_cluster_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response