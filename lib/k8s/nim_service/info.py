class K8sNimServiceInfo():
    def __init__(self):
        self.nim_service = None

    def get_nim_service_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_nim_services(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'nim_service', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_nim_service(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'nim_service', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_nim_service(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_nim_service(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_nim_service(self, cache_enabled=True):
        infos = self.get_nim_services(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True