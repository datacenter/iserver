class K8sMetalLbInfo():
    def __init__(self):
        self.metallb = None

    def get_metallb_info(self, managed_object):
        return self.get_base_info(managed_object)

    def get_metallbs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'metallb', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_metallb(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_metallb(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_metallb(self, cache_enabled=True):
        policies = self.get_metallbs(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_any_metallb(self, cache_enabled=True):
        policies = self.get_metallbs(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return None
        return policies[0]
    
    def get_metallb(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'metallb', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
