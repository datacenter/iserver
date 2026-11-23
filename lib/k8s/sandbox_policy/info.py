class K8sSandboxPolicyInfo():
    def __init__(self):
        self.sandbox_policy = None

    def get_sandbox_policy_info(self, managed_object):
        return self.get_base_info(managed_object)
        
    def get_sandbox_policys(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'sandbox_policy', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_sandbox_policy(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'sandbox_policy', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_sandbox_policy(self, name, cache_enabled=True, optimized=True):
        if self.get_sandbox_policy(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_sandbox_policy(self, cache_enabled=True):
        infos = self.get_sandbox_policys(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True