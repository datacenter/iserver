class K8sTracingPolicyNamespacedInfo():
    def __init__(self):
        self.tracing_policy_namespaced = None

    def get_tracing_policy_namespaced_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_tracing_policy_namespaceds(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'tracing_policy_namespaced', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_tracing_policy_namespaced(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'tracing_policy_namespaced', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_tracing_policy_namespaced(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_tracing_policy_namespaced(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_tracing_policy_namespaced(self, cache_enabled=True):
        infos = self.get_tracing_policy_namespaceds(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True