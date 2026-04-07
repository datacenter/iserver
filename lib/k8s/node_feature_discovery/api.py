class K8sNodeFeatureDiscoveryApi():
    def __init__(self):
        self.node_feature_discovery_mo = None
        self.node_feature_discovery_namespace_mo = {}

    def get_node_feature_discovery_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.node_feature_discovery_mo,
            self.node_feature_discovery_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.node_feature_discovery_mo, self.node_feature_discovery_namespace_mo = self.get_namespaced_resources(
            'NodeFeatureDiscovery', 
            'nfd.openshift.io/v1', 
            self.node_feature_discovery_mo,
            self.node_feature_discovery_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_node_feature_discovery_mo(self, namespace, name):
        return self.delete_resource('NodeFeatureDiscovery', 'nfd.openshift.io/v1', name, namespace=namespace)
