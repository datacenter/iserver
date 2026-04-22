class K8sNodeFeatureDiscoveryInfo():
    def __init__(self):
        self.node_feature_discovery = None

    def get_node_feature_discovery_info(self, managed_object):
        return self.get_base_info(managed_object)

    def get_node_feature_discoverys(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'node_feature_discovery', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_node_feature_discovery(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_node_feature_discovery(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_node_feature_discovery(self, cache_enabled=True):
        policies = self.get_node_feature_discoverys(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_node_feature_discovery(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'node_feature_discovery', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
