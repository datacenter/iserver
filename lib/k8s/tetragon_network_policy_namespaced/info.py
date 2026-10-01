class K8sTetragonNetworkPolicyNamespacedInfo():
    def __init__(self):
        self.tetragon_network_policy_namespaced = None

    def get_tetragon_network_policy_namespaced_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_tetragon_network_policy_namespaceds(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'tetragon_network_policy_namespaced', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_tetragon_network_policy_namespaced(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'tetragon_network_policy_namespaced', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_tetragon_network_policy_namespaced(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_tetragon_network_policy_namespaced(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_tetragon_network_policy_namespaced(self, cache_enabled=True):
        infos = self.get_tetragon_network_policy_namespaceds(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True