class K8sNemoGuardrailInfo():
    def __init__(self):
        self.nemo_guardrail = None

    def get_AAA_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_AAAs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'AAA', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_AAA(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'AAA', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_AAA(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_AAA(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_AAA(self, cache_enabled=True):
        infos = self.get_AAAs(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True