class K8sNodeFeatureApi():
    def __init__(self):
        self.node_feature_mo = None
        self.node_feature_namespace_mo = {}

    def get_node_feature_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.node_feature_mo,
            self.node_feature_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.node_feature_mo, self.node_feature_namespace_mo = self.get_namespaced_resources(
            'NodeFeature', 
            'nfd.openshift.io/v1alpha1', 
            self.node_feature_mo,
            self.node_feature_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response